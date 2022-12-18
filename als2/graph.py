class Vertex:
    def __init__(self, val):
        self.Value = val


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        if None not in self.vertex:
            return False
        index = self.vertex.index(None)
        self.vertex[index] = Vertex(v)

    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in self.m_adjacency:
            i[v] = 0
        self.m_adjacency[v] = [0] * self.max_vertex

    def IsEdge(self, v1, v2):
        return True if self.m_adjacency[v1][v2] else False

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
