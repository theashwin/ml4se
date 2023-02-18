public synchronized void remapNode(@NonNull Node node) {
        version++;

        if (buildMode == MeshBuildMode.MESH) {
            node.getUpstreamNode().removeFromDownstreams(node);

            boolean m = false;
            for (val n : sortedNodes) {
                // we dont want to remap node to itself
                if (!Objects.equals(n, node) && n.status().equals(NodeStatus.ONLINE)) {
                    n.addDownstreamNode(node);
                    m = true;
                    break;
                }
            }

            // if we were unable to find good enough node - we'll map this node to the rootNode
            if (!m) {
                rootNode.addDownstreamNode(node);
            }

            // i hope we won't deadlock here? :)
            synchronized (this) {
                Collections.sort(sortedNodes);
            }
        } else if (buildMode == MeshBuildMode.PLAIN) {
            // nothing to do here
        }
    }