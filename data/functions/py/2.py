def new_vertex(self):
    """Creates and returns a new vertex.

    Returns:
      A new Vertex instance with a unique index.
    """
    vertex = Vertex(len(self.vertices))
    self.vertices.append(vertex)
    return vertex