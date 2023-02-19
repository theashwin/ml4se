def rounding_sequence_accuracy(predictions,
                               labels,
                               weights_fn=common_layers.weights_nonzero):
  """Sequence accuracy for L1/L2 losses: round down the predictions to ints."""
  outputs = tf.squeeze(tf.to_int32(predictions), axis=-1)
  weights = weights_fn(labels)
  labels = tf.to_int32(labels)
  not_correct = tf.to_float(tf.not_equal(outputs, labels)) * weights
  axis = list(range(1, len(outputs.get_shape())))
  correct_seq = 1.0 - tf.minimum(1.0, tf.reduce_sum(not_correct, axis=axis))
  return correct_seq, tf.constant(1.0)