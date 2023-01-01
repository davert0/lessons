class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


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

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        stack = []
        current_vertex = self.vertex[VFrom]
        current_vertex.Hit = True
        stack.append(current_vertex)
        for i in self.m_adjacency[VFrom]:
            if i == 1 and self.vertex[i] == self.vertex[VTo]:
                stack.append(self.vertex[VTo])
                return stack
        for i in self.m_adjacency[VFrom]:
            if i == 1 and self.vertex[i].Hit == False:
                return stack + self.DepthFirstSearch(VFrom=i, VTo=VTo)
        stack.pop()
        return stack
