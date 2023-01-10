from graph import SimpleGraph, Vertex
import pytest

@pytest.fixture
def full_graph_no_edges() -> SimpleGraph:
    graph = SimpleGraph(5)
    graph.AddVertex(Vertex("A"))
    graph.AddVertex(Vertex("B"))
    graph.AddVertex(Vertex("C"))
    graph.AddVertex(Vertex("D"))
    graph.AddVertex(Vertex("E"))
    return graph

@pytest.fixture
def full_graph(full_graph_no_edges: SimpleGraph):
    full_graph_no_edges.AddEdge(0, 1)
    full_graph_no_edges.AddEdge(0, 2)
    full_graph_no_edges.AddEdge(0, 3)
    full_graph_no_edges.AddEdge(1, 3)
    full_graph_no_edges.AddEdge(1, 4)
    full_graph_no_edges.AddEdge(2, 3)
    full_graph_no_edges.AddEdge(3, 3)
    full_graph_no_edges.AddEdge(3, 4)
    return full_graph_no_edges


# def test_dfs_0_4(full_graph: SimpleGraph):
#     path: list = full_graph.DepthFirstSearch(0, 4)
#     assert [0, 1, 4] == [vertex.Index for vertex in path]

def test_bfs(full_graph: SimpleGraph):
    path = full_graph.BreadthFirstSearch(0, 4)
    assert ["A", "B", "E"] == [vertex.Value for vertex in path]