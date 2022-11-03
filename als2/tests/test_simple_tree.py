from logging import root
import pytest
from simple_tree import SimpleTree, SimpleTreeNode

@pytest.fixture
def root_node():
    return SimpleTreeNode(0, None)

@pytest.fixture
def tree(root_node):
    return SimpleTree(root_node)


@pytest.fixture
def child_node(root_node):
    new_child = SimpleTreeNode(1, root_node)
    return new_child

@pytest.fixture
def tree_with_two_nodes(tree, root_node, child_node):
    tree.AddChild(root_node, child_node)
    return tree

@pytest.fixture
def tree_with_six_nodes(tree, root_node):
    child_1 = SimpleTreeNode(1, root_node)
    child_2 = SimpleTreeNode(2, child_1)
    child_3 = SimpleTreeNode(3, root_node)
    child_4 = SimpleTreeNode(4, root_node)
    child_5 = SimpleTreeNode(5, child_2)
    tree.AddChild(root_node, child_1)
    tree.AddChild(child_1, child_2)
    tree.AddChild(root_node, child_3)
    tree.AddChild(root_node, child_4)
    tree.AddChild(child_2, child_5)
    return tree

@pytest.fixture
def tree_with_doubling_nodes(tree_with_six_nodes, root_node):
    child_1 = SimpleTreeNode(1, root_node)
    child_2 = SimpleTreeNode(2, child_1)
    child_3 = SimpleTreeNode(2, root_node)
    tree_with_six_nodes.AddChild(root_node, child_1)
    tree_with_six_nodes.AddChild(child_1, child_2)
    tree_with_six_nodes.AddChild(root_node, child_3)
    return tree_with_six_nodes

def test_add_child(tree, root_node):
    new_child = SimpleTreeNode(1, root_node)
    tree.AddChild(root_node, new_child)
    assert new_child.Parent == root_node
    assert new_child in root_node.Children


def test_delete_node(tree_with_two_nodes, child_node):
    tree_with_two_nodes.DeleteNode(child_node)
    assert child_node.Parent == None
    assert tree_with_two_nodes.Root.Children == []

def test_get_all_nodes(tree_with_six_nodes):
    assert len(tree_with_six_nodes.GetAllNodes()) == 6
    nodes_values = [node.NodeValue for node in tree_with_six_nodes.GetAllNodes()]
    for i in range(5):
        assert i in nodes_values


def test_find_nodes_by_value(tree_with_doubling_nodes):
    assert len(tree_with_doubling_nodes.FindNodesByValue(0)) == 1
    assert len(tree_with_doubling_nodes.FindNodesByValue(1)) == 2
    assert len(tree_with_doubling_nodes.FindNodesByValue(2)) == 3

def test_move_node(tree, root_node):
    child_1 = SimpleTreeNode(1, root_node)
    child_2 = SimpleTreeNode(2, child_1)
    child_3 = SimpleTreeNode(3, root_node)
    child_4 = SimpleTreeNode(4, root_node)
    child_5 = SimpleTreeNode(5, child_2)
    tree.AddChild(root_node, child_1)
    tree.AddChild(child_1, child_2)
    tree.AddChild(root_node, child_3)
    tree.AddChild(root_node, child_4)
    tree.AddChild(child_2, child_5)
    assert child_1 in root_node.Children
    tree.MoveNode(child_1, child_3)
    assert child_1 not in root_node.Children
    assert child_1 in child_3.Children
    assert child_1.Parent == child_3

def test_count_six(tree_with_six_nodes):
    assert tree_with_six_nodes.Count() == 6

def test_count_nine(tree_with_doubling_nodes):
    assert tree_with_doubling_nodes.Count() == 9

def test_leaf_count(tree_with_six_nodes):
    assert tree_with_six_nodes.LeafCount() == 3