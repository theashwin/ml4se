def write_data(self, chunksize, dropna=False):
        """ we form the data into a 2-d including indexes,values,mask
            write chunk-by-chunk """

        names = self.dtype.names
        nrows = self.nrows_expected

        # if dropna==True, then drop ALL nan rows
        masks = []
        if dropna:

            for a in self.values_axes:

                # figure the mask: only do if we can successfully process this
                # column, otherwise ignore the mask
                mask = isna(a.data).all(axis=0)
                if isinstance(mask, np.ndarray):
                    masks.append(mask.astype('u1', copy=False))

        # consolidate masks
        if len(masks):
            mask = masks[0]
            for m in masks[1:]:
                mask = mask & m
            mask = mask.ravel()
        else:
            mask = None

        # broadcast the indexes if needed
        indexes = [a.cvalues for a in self.index_axes]
        nindexes = len(indexes)
        bindexes = []
        for i, idx in enumerate(indexes):

            # broadcast to all other indexes except myself
            if i > 0 and i < nindexes:
                repeater = np.prod(
                    [indexes[bi].shape[0] for bi in range(0, i)])
                idx = np.tile(idx, repeater)

            if i < nindexes - 1:
                repeater = np.prod([indexes[bi].shape[0]
                                    for bi in range(i + 1, nindexes)])
                idx = np.repeat(idx, repeater)

            bindexes.append(idx)

        # transpose the values so first dimension is last
        # reshape the values if needed
        values = [a.take_data() for a in self.values_axes]
        values = [v.transpose(np.roll(np.arange(v.ndim), v.ndim - 1))
                  for v in values]
        bvalues = []
        for i, v in enumerate(values):
            new_shape = (nrows,) + self.dtype[names[nindexes + i]].shape
            bvalues.append(values[i].reshape(new_shape))

        # write the chunks
        if chunksize is None:
            chunksize = 100000

        rows = np.empty(min(chunksize, nrows), dtype=self.dtype)
        chunks = int(nrows / chunksize) + 1
        for i in range(chunks):
            start_i = i * chunksize
            end_i = min((i + 1) * chunksize, nrows)
            if start_i >= end_i:
                break

            self.write_data_chunk(
                rows,
                indexes=[a[start_i:end_i] for a in bindexes],
                mask=mask[start_i:end_i] if mask is not None else None,
                values=[v[start_i:end_i] for v in bvalues])