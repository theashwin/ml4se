def attach_pipeline(self, pipeline, name, chunks=None, eager=True):
        """Register a pipeline to be computed at the start of each day.

        Parameters
        ----------
        pipeline : Pipeline
            The pipeline to have computed.
        name : str
            The name of the pipeline.
        chunks : int or iterator, optional
            The number of days to compute pipeline results for. Increasing
            this number will make it longer to get the first results but
            may improve the total runtime of the simulation. If an iterator
            is passed, we will run in chunks based on values of the iterator.
            Default is True.
        eager : bool, optional
            Whether or not to compute this pipeline prior to
            before_trading_start.

        Returns
        -------
        pipeline : Pipeline
            Returns the pipeline that was attached unchanged.

        See Also
        --------
        :func:`zipline.api.pipeline_output`
        """
        if chunks is None:
            # Make the first chunk smaller to get more immediate results:
            # (one week, then every half year)
            chunks = chain([5], repeat(126))
        elif isinstance(chunks, int):
            chunks = repeat(chunks)

        if name in self._pipelines:
            raise DuplicatePipelineName(name=name)

        self._pipelines[name] = AttachedPipeline(pipeline, iter(chunks), eager)

        # Return the pipeline to allow expressions like
        # p = attach_pipeline(Pipeline(), 'name')
        return pipeline