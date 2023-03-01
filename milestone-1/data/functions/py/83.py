def cyclegan_upsample(net, num_outputs, stride, method="conv2d_transpose"):
  """Upsamples the given inputs.

  Args:
    net: A Tensor of size [batch_size, height, width, filters].
    num_outputs: The number of output filters.
    stride: A list of 2 scalars or a 1x2 Tensor indicating the scale,
      relative to the inputs, of the output dimensions. For example, if kernel
      size is [2, 3], then the output height and width will be twice and three
      times the input size.
    method: The upsampling method: 'nn_upsample_conv',
      'bilinear_upsample_conv', or 'conv2d_transpose'.

  Returns:
    A Tensor which was upsampled using the specified method.

  Raises:
    ValueError: if `method` is not recognized.
  """

  with tf.variable_scope("upconv"):
    net_shape = tf.shape(net)
    height = net_shape[1]
    width = net_shape[2]

    # Reflection pad by 1 in spatial dimensions (axes 1, 2 = h, w) to make a
    # 3x3 "valid" convolution produce an output with the same dimension as the
    # input.
    spatial_pad_1 = np.array([[0, 0], [1, 1], [1, 1], [0, 0]])

    if method == "nn_upsample_conv":
      net = tf.image.resize_nearest_neighbor(
          net, [stride[0] * height, stride[1] * width])
      net = tf.pad(net, spatial_pad_1, "REFLECT")
      net = layers().Conv2D(
          num_outputs, (3, 3), activation=tf.nn.relu)(net)
    elif method == "bilinear_upsample_conv":
      net = tf.image.resize_bilinear(net,
                                     [stride[0] * height, stride[1] * width])
      net = tf.pad(net, spatial_pad_1, "REFLECT")
      net = layers().Conv2D(
          num_outputs, (3, 3), activation=tf.nn.relu)(net)
    elif method == "conv2d_transpose":
      # This corrects 1 pixel offset for images with even width and height.
      # conv2d is left aligned and conv2d_transpose is right aligned for even
      # sized images (while doing "SAME" padding).
      # Note: This doesn"t reflect actual model in paper.
      net = layers().Conv2DTranspose(
          num_outputs, (3, 3), strides=stride, activation=tf.nn.relu)(net)
      net = net[:, 1:, 1:, :]
    else:
      raise ValueError("Unknown method: [%s]" % method)

    return net