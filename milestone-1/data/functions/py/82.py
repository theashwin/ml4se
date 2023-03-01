def load_data(self, sess, inputs, state_inputs):
        """Bulk loads the specified inputs into device memory.

        The shape of the inputs must conform to the shapes of the input
        placeholders this optimizer was constructed with.

        The data is split equally across all the devices. If the data is not
        evenly divisible by the batch size, excess data will be discarded.

        Args:
            sess: TensorFlow session.
            inputs: List of arrays matching the input placeholders, of shape
                [BATCH_SIZE, ...].
            state_inputs: List of RNN input arrays. These arrays have size
                [BATCH_SIZE / MAX_SEQ_LEN, ...].

        Returns:
            The number of tuples loaded per device.
        """

        if log_once("load_data"):
            logger.info(
                "Training on concatenated sample batches:\n\n{}\n".format(
                    summarize({
                        "placeholders": self.loss_inputs,
                        "inputs": inputs,
                        "state_inputs": state_inputs
                    })))

        feed_dict = {}
        assert len(self.loss_inputs) == len(inputs + state_inputs), \
            (self.loss_inputs, inputs, state_inputs)

        # Let's suppose we have the following input data, and 2 devices:
        # 1 2 3 4 5 6 7                              <- state inputs shape
        # A A A B B B C C C D D D E E E F F F G G G  <- inputs shape
        # The data is truncated and split across devices as follows:
        # |---| seq len = 3
        # |---------------------------------| seq batch size = 6 seqs
        # |----------------| per device batch size = 9 tuples

        if len(state_inputs) > 0:
            smallest_array = state_inputs[0]
            seq_len = len(inputs[0]) // len(state_inputs[0])
            self._loaded_max_seq_len = seq_len
        else:
            smallest_array = inputs[0]
            self._loaded_max_seq_len = 1

        sequences_per_minibatch = (
            self.max_per_device_batch_size // self._loaded_max_seq_len * len(
                self.devices))
        if sequences_per_minibatch < 1:
            logger.warn(
                ("Target minibatch size is {}, however the rollout sequence "
                 "length is {}, hence the minibatch size will be raised to "
                 "{}.").format(self.max_per_device_batch_size,
                               self._loaded_max_seq_len,
                               self._loaded_max_seq_len * len(self.devices)))
            sequences_per_minibatch = 1

        if len(smallest_array) < sequences_per_minibatch:
            # Dynamically shrink the batch size if insufficient data
            sequences_per_minibatch = make_divisible_by(
                len(smallest_array), len(self.devices))

        if log_once("data_slicing"):
            logger.info(
                ("Divided {} rollout sequences, each of length {}, among "
                 "{} devices.").format(
                     len(smallest_array), self._loaded_max_seq_len,
                     len(self.devices)))

        if sequences_per_minibatch < len(self.devices):
            raise ValueError(
                "Must load at least 1 tuple sequence per device. Try "
                "increasing `sgd_minibatch_size` or reducing `max_seq_len` "
                "to ensure that at least one sequence fits per device.")
        self._loaded_per_device_batch_size = (sequences_per_minibatch // len(
            self.devices) * self._loaded_max_seq_len)

        if len(state_inputs) > 0:
            # First truncate the RNN state arrays to the sequences_per_minib.
            state_inputs = [
                make_divisible_by(arr, sequences_per_minibatch)
                for arr in state_inputs
            ]
            # Then truncate the data inputs to match
            inputs = [arr[:len(state_inputs[0]) * seq_len] for arr in inputs]
            assert len(state_inputs[0]) * seq_len == len(inputs[0]), \
                (len(state_inputs[0]), sequences_per_minibatch, seq_len,
                 len(inputs[0]))
            for ph, arr in zip(self.loss_inputs, inputs + state_inputs):
                feed_dict[ph] = arr
            truncated_len = len(inputs[0])
        else:
            for ph, arr in zip(self.loss_inputs, inputs + state_inputs):
                truncated_arr = make_divisible_by(arr, sequences_per_minibatch)
                feed_dict[ph] = truncated_arr
                truncated_len = len(truncated_arr)

        sess.run([t.init_op for t in self._towers], feed_dict=feed_dict)

        self.num_tuples_loaded = truncated_len
        tuples_per_device = truncated_len // len(self.devices)
        assert tuples_per_device > 0, "No data loaded?"
        assert tuples_per_device % self._loaded_per_device_batch_size == 0
        return tuples_per_device