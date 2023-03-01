def read_feather(cls, path, columns=None, use_threads=True):
        """Read a pandas.DataFrame from Feather format.
           Ray DataFrame only supports pyarrow engine for now.

        Args:
            path: The filepath of the feather file.
                  We only support local files for now.
                multi threading is set to True by default
            columns: not supported by pandas api, but can be passed here to read only
                specific columns
            use_threads: Whether or not to use threads when reading

        Notes:
            pyarrow feather is used. Please refer to the documentation here
            https://arrow.apache.org/docs/python/api.html#feather-format
        """
        if cls.read_feather_remote_task is None:
            return super(RayIO, cls).read_feather(
                path, columns=columns, use_threads=use_threads
            )

        if columns is None:
            from pyarrow.feather import FeatherReader

            fr = FeatherReader(path)
            columns = [fr.get_column_name(i) for i in range(fr.num_columns)]

        num_partitions = cls.frame_mgr_cls._compute_num_partitions()
        num_splits = min(len(columns), num_partitions)
        # Each item in this list will be a list of column names of the original df
        column_splits = (
            len(columns) // num_partitions
            if len(columns) % num_partitions == 0
            else len(columns) // num_partitions + 1
        )
        col_partitions = [
            columns[i : i + column_splits]
            for i in range(0, len(columns), column_splits)
        ]
        blk_partitions = np.array(
            [
                cls.read_feather_remote_task._remote(
                    args=(path, cols, num_splits), num_return_vals=num_splits + 1
                )
                for cols in col_partitions
            ]
        ).T
        remote_partitions = np.array(
            [
                [cls.frame_partition_cls(obj) for obj in row]
                for row in blk_partitions[:-1]
            ]
        )
        index_len = ray.get(blk_partitions[-1][0])
        index = pandas.RangeIndex(index_len)
        new_query_compiler = cls.query_compiler_cls(
            cls.frame_mgr_cls(remote_partitions), index, columns
        )
        return new_query_compiler