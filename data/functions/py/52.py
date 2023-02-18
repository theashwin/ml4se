def get_gated_grpc_tensors(self, matching_debug_op=None):
    """Extract all nodes with gated-gRPC debug ops attached.

    Uses cached values if available.
    This method is thread-safe.

    Args:
      graph_def: A tf.GraphDef proto.
      matching_debug_op: Return tensors and nodes with only matching the
        specified debug op name (optional). If `None`, will extract only
        `DebugIdentity` debug ops.

    Returns:
      A list of (node_name, op_type, output_slot, debug_op) tuples.
    """
    with self._grpc_gated_lock:
      matching_debug_op = matching_debug_op or 'DebugIdentity'
      if matching_debug_op not in self._grpc_gated_tensors:
        # First, construct a map from node name to op type.
        node_name_to_op_type = dict(
            (node.name, node.op) for node in self._graph_def.node)

        # Second, populate the output list.
        gated = []
        for node in self._graph_def.node:
          if node.op == matching_debug_op:
            for attr_key in node.attr:
              if attr_key == 'gated_grpc' and node.attr[attr_key].b:
                node_name, output_slot, _, debug_op = (
                    debug_graphs.parse_debug_node_name(node.name))
                gated.append(
                    (node_name, node_name_to_op_type[node_name], output_slot,
                     debug_op))
                break
        self._grpc_gated_tensors[matching_debug_op] = gated

      return self._grpc_gated_tensors[matching_debug_op]