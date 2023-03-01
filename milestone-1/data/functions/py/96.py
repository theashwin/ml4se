def get_loc(self, key, method=None):
        """
        Get location for a label or a tuple of labels as an integer, slice or
        boolean mask.

        Parameters
        ----------
        key : label or tuple of labels (one for each level)
        method : None

        Returns
        -------
        loc : int, slice object or boolean mask
            If the key is past the lexsort depth, the return may be a
            boolean mask array, otherwise it is always a slice or int.

        Examples
        ---------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')])

        >>> mi.get_loc('b')
        slice(1, 3, None)

        >>> mi.get_loc(('b', 'e'))
        1

        Notes
        ------
        The key cannot be a slice, list of same-level labels, a boolean mask,
        or a sequence of such. If you want to use those, use
        :meth:`MultiIndex.get_locs` instead.

        See Also
        --------
        Index.get_loc : The get_loc method for (single-level) index.
        MultiIndex.slice_locs : Get slice location given start label(s) and
                                end label(s).
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.
        """
        if method is not None:
            raise NotImplementedError('only the default get_loc method is '
                                      'currently supported for MultiIndex')

        def _maybe_to_slice(loc):
            """convert integer indexer to boolean mask or slice if possible"""
            if not isinstance(loc, np.ndarray) or loc.dtype != 'int64':
                return loc

            loc = lib.maybe_indices_to_slice(loc, len(self))
            if isinstance(loc, slice):
                return loc

            mask = np.empty(len(self), dtype='bool')
            mask.fill(False)
            mask[loc] = True
            return mask

        if not isinstance(key, tuple):
            loc = self._get_level_indexer(key, level=0)
            return _maybe_to_slice(loc)

        keylen = len(key)
        if self.nlevels < keylen:
            raise KeyError('Key length ({0}) exceeds index depth ({1})'
                           ''.format(keylen, self.nlevels))

        if keylen == self.nlevels and self.is_unique:
            return self._engine.get_loc(key)

        # -- partial selection or non-unique index
        # break the key into 2 parts based on the lexsort_depth of the index;
        # the first part returns a continuous slice of the index; the 2nd part
        # needs linear search within the slice
        i = self.lexsort_depth
        lead_key, follow_key = key[:i], key[i:]
        start, stop = (self.slice_locs(lead_key, lead_key)
                       if lead_key else (0, len(self)))

        if start == stop:
            raise KeyError(key)

        if not follow_key:
            return slice(start, stop)

        warnings.warn('indexing past lexsort depth may impact performance.',
                      PerformanceWarning, stacklevel=10)

        loc = np.arange(start, stop, dtype='int64')

        for i, k in enumerate(follow_key, len(lead_key)):
            mask = self.codes[i][loc] == self.levels[i].get_loc(k)
            if not mask.all():
                loc = loc[mask]
            if not len(loc):
                raise KeyError(key)

        return (_maybe_to_slice(loc) if len(loc) != stop - start else
                slice(start, stop))