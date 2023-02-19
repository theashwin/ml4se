def __prepare_dataset_parameter(self, dataset):
        """
        Processes the dataset parameter for type correctness.
        Returns it as an SFrame.
        """

        # Translate the dataset argument into the proper type
        if not isinstance(dataset, _SFrame):
            def raise_dataset_type_exception():
                raise TypeError("The dataset parameter must be either an SFrame, "
                                "or a dictionary of (str : list) or (str : value).")

            if type(dataset) is dict:
                if not all(type(k) is str for k in _six.iterkeys(dataset)):
                    raise_dataset_type_exception()

                if all(type(v) in (list, tuple, _array.array) for v in _six.itervalues(dataset)):
                    dataset = _SFrame(dataset)
                else:
                    dataset = _SFrame({k : [v] for k, v in _six.iteritems(dataset)})
            else:
                raise_dataset_type_exception()

        return dataset