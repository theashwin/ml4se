def _init_vocab(self, token_generator, add_reserved_tokens=True):
    """Initialize vocabulary with tokens from token_generator."""

    self._id_to_token = {}
    non_reserved_start_index = 0

    if add_reserved_tokens:
      self._id_to_token.update(enumerate(RESERVED_TOKENS))
      non_reserved_start_index = len(RESERVED_TOKENS)

    self._id_to_token.update(
        enumerate(token_generator, start=non_reserved_start_index))

    # _token_to_id is the reverse of _id_to_token
    self._token_to_id = dict((v, k)
                             for k, v in six.iteritems(self._id_to_token))