def cub200_iterator(data_path, batch_k, batch_size, data_shape):
    """Return training and testing iterator for the CUB200-2011 dataset."""
    return (CUB200Iter(data_path, batch_k, batch_size, data_shape, is_train=True),
            CUB200Iter(data_path, batch_k, batch_size, data_shape, is_train=False))