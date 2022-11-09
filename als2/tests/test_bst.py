import pytest
from bst import BST, BSTFind, BSTNode

@pytest.fixture
def tree_with_15_nodes():
    root = BSTNode(8, 8, None)
    node_4 = BSTNode(4, 4, root)
    node_12 = BSTNode(12, 12, root)
    root.LeftChild = node_4
    root.RightChild = node_12

    node_2 = BSTNode(2, 2, node_4)
    node_6 = BSTNode(6, 6, node_4)
    node_4.LeftChild = node_2
    node_4.RightChild = node_6

    node_1 = BSTNode(1, 1, node_2)
    node_3 = BSTNode(3,3, node_2)
    node_2.LeftChild = node_1
    node_2.RightChild = node_3

    node_5 = BSTNode(5, 5, node_6)
    node_7 = BSTNode(7, 7, node_6)
    node_6.LeftChild = node_5
    node_6.RightChild = node_7

    node_10 = BSTNode(10, 10, node_12)
    node_14 = BSTNode(14, 14, node_12)
    node_12.LeftChild = node_10
    node_12.RightChild = node_14

    node_9 = BSTNode(9, 9, node_10)
    node_11 = BSTNode(11, 11, node_10)
    node_10.LeftChild = node_9
    node_10.RightChild = node_11

    node_13 = BSTNode(13, 13, node_14)
    node_15 = BSTNode(15, 15, node_14)
    node_14.LeftChild = node_13
    node_14.RightChild = node_15


def test_find():
    root = BSTNode(8, 8, None)
    node_4 = BSTNode(4, 4, root)
    node_12 = BSTNode(12, 12, root)
    root.LeftChild = node_4
    root.RightChild = node_12

    node_2 = BSTNode(2, 2, node_4)
    node_6 = BSTNode(6, 6, node_4)
    node_4.LeftChild = node_2
    node_4.RightChild = node_6

    node_1 = BSTNode(1, 1, node_2)
    node_3 = BSTNode(3,3, node_2)
    node_2.LeftChild = node_1
    node_2.RightChild = node_3

    node_5 = BSTNode(5, 5, node_6)
    node_7 = BSTNode(7, 7, node_6)
    node_6.LeftChild = node_5
    node_6.RightChild = node_7

    node_10 = BSTNode(10, 10, node_12)
    node_14 = BSTNode(14, 14, node_12)
    node_12.LeftChild = node_10
    node_12.RightChild = node_14

    node_9 = BSTNode(9, 9, node_10)
    node_11 = BSTNode(11, 11, node_10)
    node_10.LeftChild = node_9
    node_10.RightChild = node_11

    node_13 = BSTNode(13, 13, node_14)
    node_15 = BSTNode(15, 15, node_14)
    node_14.LeftChild = node_13
    node_14.RightChild = node_15

    bst = BST(root)

    node_3_find_expected = BSTFind()
    node_3_find_expected.Node = node_3
    node_3_find_expected.NodeHasKey = True
    node_3_find_real = bst.FindNodeByKey(3)
    assert node_3_find_expected.Node == node_3_find_real.Node
    assert node_3_find_expected.NodeHasKey == node_3_find_real.NodeHasKey
    assert node_3_find_expected.ToLeft == node_3_find_real.ToLeft


    empty_find_expected = BSTFind()
    empty_bst = BST(None)
    empty_find_real = empty_bst.FindNodeByKey(5)
    assert empty_find_expected.Node == empty_find_real.Node
    assert empty_find_expected.NodeHasKey == empty_find_real.NodeHasKey
    assert empty_find_expected.ToLeft == empty_find_real.ToLeft

    node_3_find_expected = BSTFind()
    node_3_find_expected.Node = node_3
    node_3_find_expected.NodeHasKey = True
    node_3_find_real = bst.FindNodeByKey(3)
    assert node_3_find_expected.Node == node_3_find_real.Node
    assert node_3_find_expected.NodeHasKey == node_3_find_real.NodeHasKey
    assert node_3_find_expected.ToLeft == node_3_find_real.ToLeft

    node_13_find_expected = BSTFind()
    node_13_find_expected.Node = node_13
    node_13_find_expected.NodeHasKey = True
    node_13_find_expected.ToLeft = True
    node_13_find_real = bst.FindNodeByKey(13)
    assert node_13_find_expected.Node == node_13_find_real.Node
    assert node_13_find_expected.NodeHasKey == node_13_find_real.NodeHasKey
    assert node_13_find_expected.ToLeft == node_13_find_real.ToLeft

    node_minus_one_find_expected = BSTFind()
    node_minus_one_find_expected.Node = node_1
    node_minus_one_find_expected.ToLeft = True
    node_minus_one_find_real = bst.FindNodeByKey(-1)
    assert node_minus_one_find_expected.Node == node_minus_one_find_real.Node
    assert node_minus_one_find_expected.NodeHasKey == node_minus_one_find_real.NodeHasKey
    assert node_minus_one_find_expected.ToLeft == node_minus_one_find_real.ToLeft


    node_16_find_expected = BSTFind()
    node_16_find_expected.Node = node_15
    node_16_find_expected_real = bst.FindNodeByKey(16)
    assert node_16_find_expected.Node == node_16_find_expected_real.Node
    assert node_16_find_expected.NodeHasKey == node_16_find_expected_real.NodeHasKey
    assert node_16_find_expected.ToLeft == node_16_find_expected_real.ToLeft

def test_add_key_value():
    root = BSTNode(8, 8, None)
    node_4 = BSTNode(4, 4, root)
    node_12 = BSTNode(12, 12, root)
    root.LeftChild = node_4
    root.RightChild = node_12

    node_2 = BSTNode(2, 2, node_4)
    node_6 = BSTNode(6, 6, node_4)
    node_4.LeftChild = node_2
    node_4.RightChild = node_6

    node_1 = BSTNode(1, 1, node_2)
    node_3 = BSTNode(3,3, node_2)
    node_2.LeftChild = node_1
    node_2.RightChild = node_3

    node_5 = BSTNode(5, 5, node_6)
    node_7 = BSTNode(7, 7, node_6)
    node_6.LeftChild = node_5
    node_6.RightChild = node_7

    node_10 = BSTNode(10, 10, node_12)
    node_14 = BSTNode(14, 14, node_12)
    node_12.LeftChild = node_10
    node_12.RightChild = node_14

    node_9 = BSTNode(9, 9, node_10)
    node_11 = BSTNode(11, 11, node_10)
    node_10.LeftChild = node_9
    node_10.RightChild = node_11

    node_13 = BSTNode(13, 13, node_14)
    node_15 = BSTNode(15, 15, node_14)
    node_14.LeftChild = node_13
    node_14.RightChild = node_15

    bst = BST(root)

    assert bst.AddKeyValue(15, 15) == False

    assert bst.FindNodeByKey(16).NodeHasKey == False
    bst.AddKeyValue(16, 16)
    assert bst.FindNodeByKey(16).NodeHasKey == True
    assert bst.FindNodeByKey(16).ToLeft == False

    assert bst.FindNodeByKey(-1).NodeHasKey == False
    bst.AddKeyValue(-1, -1)
    assert bst.FindNodeByKey(-1).NodeHasKey == True
    assert bst.FindNodeByKey(-1).ToLeft == True
    
