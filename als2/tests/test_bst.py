import pytest
from bst import *


@pytest.fixture
def bst() -> BST:
    bst = BST(BSTNode(8, 8, None))
    return bst

@pytest.fixture
def bst_full() -> BST:
    bst = BST(BSTNode(8, 8, None))
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(5, 5)
    bst.AddKeyValue(7, 7)
    return bst


def test_FindNodeByKey(bst):
    empty = BST(None)
    assert empty.FindNodeByKey(3).Node is None

    assert isinstance(bst.FindNodeByKey(8), BSTFind)
    assert bst.FindNodeByKey(8).Node.NodeKey == 8

    assert bst.FindNodeByKey(4).Node is bst.Root
    assert bst.FindNodeByKey(4).ToLeft

    assert bst.FindNodeByKey(12).Node is bst.Root
    assert not bst.FindNodeByKey(12).ToLeft


def test_AddKeyValue_bst(bst):
    assert not bst.AddKeyValue(8, 8)

    empty = BST(None)
    empty.AddKeyValue(9, 9)
    assert empty.Root.NodeKey == 9

    assert not bst.FindNodeByKey(4).NodeHasKey
    bst.AddKeyValue(4, 4)
    assert bst.FindNodeByKey(4).NodeHasKey

    assert not bst.FindNodeByKey(12).NodeHasKey
    bst.AddKeyValue(12, 12)
    assert bst.FindNodeByKey(12).NodeHasKey

    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)


def test_AddKeyValue_bst_full(bst_full):
    assert bst_full.FinMinMax(None, FindMax=True).NodeKey == 12
    assert bst_full.FinMinMax(None, FindMax=False).NodeKey == 2


def test_DeleteNodeByKey(bst_full):
    assert not bst_full.DeleteNodeByKey(14)

    bst = BST(BSTNode(8, 8, None))
    assert bst.Count() == 1
    assert bst.DeleteNodeByKey(8)
    assert bst.Count() == 0

    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(8, 8)
    bst.AddKeyValue(5, 5)
    bst.AddKeyValue(6, 6)

    bst.DeleteNodeByKey(4)

    bst_full.DeleteNodeByKey(5)
    bst_full.DeleteNodeByKey(6)
    print(bst_full)


def test_Count(bst_full):
    empty = BST(None)
    assert empty.Count() == 0

    empty.AddKeyValue(4, 4)
    assert empty.Count() == 1

    empty.AddKeyValue(5, 5)
    assert empty.Count() == 2

    assert bst_full.Count() == 7




