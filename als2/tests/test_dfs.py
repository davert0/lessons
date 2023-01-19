from graph import SimpleGraph, Vertex
import pytest


@pytest.fixture
def full_graph_no_edges() -> SimpleGraph:
    graph = SimpleGraph(6)
    graph.AddVertex(("A"))
    graph.AddVertex(("B"))
    graph.AddVertex(("C"))
    graph.AddVertex(("D"))
    graph.AddVertex(("E"))
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


@pytest.fixture
def graph_with_weak_vertex(full_graph: SimpleGraph):
    full_graph.AddVertex("F")
    full_graph.AddEdge(4, 5)
    return full_graph


def test_bfs_adjacent(full_graph: SimpleGraph):
    path = full_graph.BreadthFirstSearch(0, 1)
    assert ["A", "B"] == [vertex.Value for vertex in path]


def test_bfs(full_graph: SimpleGraph):
    path = full_graph.BreadthFirstSearch(0, 4)
    assert ["A", "D", "E"] == [vertex.Value for vertex in path]


def test_weak_vertices(graph_with_weak_vertex: SimpleGraph):
    weaks = graph_with_weak_vertex.WeakVertices()
    assert ["F"] == [vertex.Value for vertex in weaks]
