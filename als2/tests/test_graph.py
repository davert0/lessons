from graph import SimpleGraph, Vertex
import pytest

@pytest.fixture
def graph() -> SimpleGraph:
    graph = SimpleGraph(5)
    return graph

@pytest.fixture
def full_graph_no_edges() -> SimpleGraph:
    graph = SimpleGraph(5)
    graph.AddVertex(Vertex("A"))
    graph.AddVertex(Vertex("B"))
    graph.AddVertex(Vertex("C"))
    graph.AddVertex(Vertex("D"))
    graph.AddVertex(Vertex("E"))
    return graph

def test_create_graph():
    graph = SimpleGraph(5)
    assert graph
    assert graph.max_vertex == 5
    for i in graph.m_adjacency:
        assert len(i) == 5
    assert len(graph.m_adjacency) * len(graph.m_adjacency[0]) == 25
    assert len(graph.vertex) == 5

def test_create_vertex():
    vertex = Vertex("A")
    assert vertex
    assert vertex.Value == "A"

def test_add_vertex(graph: SimpleGraph):
    vert_a = "A"
    graph.AddVertex(vert_a)
    assert graph.vertex[0].Value == vert_a
    vert_b = "B"
    graph.AddVertex(vert_b)
    assert graph.vertex[1].Value == vert_b


def test_add_edge(full_graph_no_edges: SimpleGraph):
    full_graph_no_edges.AddEdge(0, 1)
    assert full_graph_no_edges.m_adjacency[0][1] == 1
    assert full_graph_no_edges.m_adjacency[1][0] == 1
    full_graph_no_edges.AddEdge(1, 2)
    assert full_graph_no_edges.m_adjacency[1][2] == 1
    assert full_graph_no_edges.m_adjacency[2][1] == 1

def test_is_edge(full_graph_no_edges: SimpleGraph):
    assert not full_graph_no_edges.IsEdge(0, 1)
    full_graph_no_edges.AddEdge(0, 1)
    assert full_graph_no_edges.IsEdge(0, 1)

def test_remove_edge(full_graph_no_edges: SimpleGraph):
    full_graph_no_edges.AddEdge(0, 1)
    assert full_graph_no_edges.IsEdge(0, 1)
    full_graph_no_edges.RemoveEdge(0, 1)
    assert not full_graph_no_edges.IsEdge(0, 1)

def test_remove_vertex(full_graph_no_edges: SimpleGraph):
    full_graph_no_edges.AddEdge(0,1)
    full_graph_no_edges.AddEdge(0,2)
    full_graph_no_edges.AddEdge(0,3)
    full_graph_no_edges.AddEdge(1,3)
    full_graph_no_edges.AddEdge(1,4)
    assert full_graph_no_edges.IsEdge(1, 0)    
    full_graph_no_edges.AddEdge(2,3)
    assert full_graph_no_edges.IsEdge(3, 0)    
    assert full_graph_no_edges.IsEdge(3, 1)    
    assert full_graph_no_edges.IsEdge(3, 2)
    full_graph_no_edges.AddEdge(3,3)
    full_graph_no_edges.AddEdge(3,4)
    assert full_graph_no_edges.IsEdge(4, 1)
    assert full_graph_no_edges.IsEdge(4, 3)
    full_graph_no_edges.RemoveVertex(3)
    assert not full_graph_no_edges.vertex[3]
    assert not full_graph_no_edges.IsEdge(0, 3)
    assert not full_graph_no_edges.IsEdge(3, 0)
    assert not full_graph_no_edges.IsEdge(1, 3)
    assert not full_graph_no_edges.IsEdge(3, 1)
    assert not full_graph_no_edges.IsEdge(2, 3)
    assert not full_graph_no_edges.IsEdge(3, 2)
    assert not full_graph_no_edges.IsEdge(3, 3)
    assert not full_graph_no_edges.IsEdge(4, 3)
    assert not full_graph_no_edges.IsEdge(3, 4)
