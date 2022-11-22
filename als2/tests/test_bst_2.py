import pytest
from bst_2 import aBST


@pytest.fixture
def abst():
    tree = aBST(3)
    tree.Tree = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]
    return tree


def test_create_bst():
    expected = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]
    keys = [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]
    tree = aBST(3)
    for key in keys:
        tree.AddKey(key)
    assert tree.Tree == expected


@pytest.mark.parametrize("input,length", [(0, 1), (1, 3), (2, 7), (3, 15)])
def test_depth(input, length):
    tree = aBST(depth=input)
    assert len(tree.Tree) == length


@pytest.mark.parametrize(
    "input,result", [(50, 0), (25, 1), (75, 2), (43, 10), (92, 14)]
)
def test_find(abst, input, result):
    assert abst.FindKeyIndex(input) == result

