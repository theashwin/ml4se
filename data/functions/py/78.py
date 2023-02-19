def _parse_example_spec(self):
    """Returns a `tf.Example` parsing spec as dict."""
    height, width = image_util.get_expected_image_size(self.module_spec)
    input_shape = [height, width, 3]
    return {self.key: tf_v1.FixedLenFeature(input_shape, tf.float32)}