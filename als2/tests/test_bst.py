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
    node_3 = BSTNode(3, 3, node_2)
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


def test_fin_min_max():
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
    node_3 = BSTNode(3, 3, node_2)
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

    assert bst.FinMinMax(node_12, FindMax=True) == node_15
    assert bst.FinMinMax(node_12, FindMax=False) == node_9


def test_count():
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
    node_3 = BSTNode(3, 3, node_2)
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

    assert bst.Count() == 15
    bst.DeleteNodeByKey(1)
    assert bst.Count() == 14
    bst.DeleteNodeByKey(3)
    assert bst.Count() == 13


import unittest


class TestBST(unittest.TestCase):
    def setUp(self):
        self.first_node_without_parent = BSTNode(5, "test", None)
        self.node_with_parent = BSTNode(3, "test3", self.first_node_without_parent)
        self.test_node1 = BSTNode(2, "test2", None)
        self.test_node2 = BSTNode(8, "test8", None)
        self.empty_tree = BST(None)
        self.test_tree1 = BST(self.first_node_without_parent)
        self.test_tree2 = BST(self.node_with_parent)
        self.full_tree = BST(self.test_node2)
        self.full_tree.AddKeyValue(4, "test4")
        self.full_tree.AddKeyValue(12, "test12")
        self.full_tree.AddKeyValue(2, "test2")
        self.full_tree.AddKeyValue(6, "test6")
        self.full_tree.AddKeyValue(10, "test10")
        self.full_tree.AddKeyValue(14, "test14")
        self.full_tree.AddKeyValue(1, "test1")
        self.full_tree.AddKeyValue(3, "test3")
        self.full_tree.AddKeyValue(5, "test5")
        self.full_tree.AddKeyValue(7, "test7")
        self.full_tree.AddKeyValue(9, "test9")
        self.full_tree.AddKeyValue(11, "test11")
        self.full_tree.AddKeyValue(13, "test13")
        self.full_tree.AddKeyValue(15, "test15")

    def test_create_tree(self):
        self.assertIsNone(self.test_tree2.Root.Parent)
        self.assertEqual(self.test_tree1.Root, self.first_node_without_parent)
        self.assertEqual(self.test_tree2.Count(), 1)
        self.assertEqual(self.empty_tree.Count(), 0)

    def test_find_node(self):
        # Тестируем ситуацию, когда искомый узел был найден
        self.finded_node = self.test_tree1.FindNodeByKey(5)
        self.assertEqual(self.finded_node.Node.NodeKey, 5)
        self.assertTrue(self.finded_node.NodeHasKey)
        # Тестируем ситуацию, когда искомый узел не был найден и новый надо добавить вправо
        self.find_node_to_right = self.test_tree2.FindNodeByKey(4)
        self.assertFalse(self.find_node_to_right.NodeHasKey)
        self.assertEqual(self.find_node_to_right.Node, self.test_tree2.Root)
        self.assertFalse(self.find_node_to_right.ToLeft)
        # Тестируем ситуацию, когда узел не был найден и новый надо добавить влево
        self.find_node_to_left = self.test_tree2.FindNodeByKey(2)
        self.assertFalse(self.find_node_to_left.NodeHasKey)
        self.assertEqual(self.find_node_to_left.Node, self.test_tree2.Root)
        self.assertTrue(self.find_node_to_left.ToLeft)

    def test_add_node(self):
        # Тестируем добавление узла левым потомком
        self.no_element_bykey = self.test_tree1.FindNodeByKey(2)
        self.assertFalse(self.no_element_bykey.NodeHasKey)
        self.assertEqual(self.no_element_bykey.Node, self.test_tree1.Root)
        self.assertTrue(self.no_element_bykey.ToLeft)
        self.assertTrue(self.test_tree1.AddKeyValue(2, "test2"))
        self.added_element_bykey = self.test_tree1.FindNodeByKey(2)
        self.assertEqual(self.added_element_bykey.Node.NodeKey, 2)
        self.assertTrue(self.added_element_bykey.NodeHasKey)
        self.assertFalse(self.added_element_bykey.ToLeft)
        # Тестируем добавление узла правым потомком
        self.no_element_bykey = self.test_tree1.FindNodeByKey(7)
        self.assertFalse(self.no_element_bykey.NodeHasKey)
        self.assertEqual(self.no_element_bykey.Node, self.test_tree1.Root)
        self.assertFalse(self.no_element_bykey.ToLeft)
        self.assertTrue(self.test_tree1.AddKeyValue(7, "test7"))
        self.added_element_bykey = self.test_tree1.FindNodeByKey(7)
        self.assertEqual(self.added_element_bykey.Node.NodeKey, 7)
        self.assertTrue(self.added_element_bykey.NodeHasKey)
        self.assertFalse(self.added_element_bykey.ToLeft)
        # Тестируем добавление первого узла в дерево
        self.no_element_bykey = self.empty_tree.FindNodeByKey(7)
        self.assertFalse(self.no_element_bykey.NodeHasKey)
        self.assertEqual(self.no_element_bykey.Node, self.empty_tree.Root)
        self.assertFalse(self.no_element_bykey.ToLeft)
        self.assertTrue(self.empty_tree.AddKeyValue(7, "test7"))
        self.added_element_bykey = self.empty_tree.FindNodeByKey(7)
        self.assertEqual(self.added_element_bykey.Node.NodeKey, 7)
        self.assertEqual(self.added_element_bykey.Node, self.empty_tree.Root)
        self.assertIsNone(self.empty_tree.Root.Parent)
        self.assertTrue(self.added_element_bykey.NodeHasKey)
        self.assertFalse(self.added_element_bykey.ToLeft)

    def test_find_min_from_root(self):
        self.finded_min = self.full_tree.FinMinMax(self.full_tree.Root, False)
        self.assertEqual(self.finded_min.NodeKey, 1)
        self.assertEqual(self.finded_min.Parent.NodeKey, 2)

    def test_find_max_from_root(self):
        self.finded_max = self.full_tree.FinMinMax(self.full_tree.Root, True)
        self.assertEqual(self.finded_max.NodeKey, 15)
        self.assertEqual(self.finded_max.Parent.NodeKey, 14)

    def test_find_min_from_node(self):
        self.start_node = self.full_tree.Root.RightChild
        self.finded_min_from_node = self.full_tree.FinMinMax(self.start_node, False)
        self.assertEqual(self.finded_min_from_node.NodeKey, 9)
        self.assertEqual(self.finded_min_from_node.Parent.NodeKey, 10)

    def test_find_max_from_node(self):
        self.start_node = self.full_tree.Root.LeftChild
        self.finded_max_from_node = self.full_tree.FinMinMax(self.start_node, True)
        self.assertEqual(self.finded_max_from_node.NodeKey, 7)
        self.assertEqual(self.finded_max_from_node.Parent.NodeKey, 6)

    def test_delete_node(self):
        self.finded_node = self.full_tree.FindNodeByKey(4)
        self.assertEqual(self.full_tree.Root.LeftChild.NodeKey, 4)
        self.assertTrue(self.finded_node.NodeHasKey)
        self.assertTrue(self.full_tree.DeleteNodeByKey(4))
        self.find_delete_node = self.full_tree.FindNodeByKey(4)
        self.assertFalse(self.find_delete_node.NodeHasKey)
        self.assertNotEqual(self.full_tree.Root.LeftChild.NodeKey, 4)
        self.assertTrue(self.full_tree.DeleteNodeByKey(8))
        self.assertTrue(self.full_tree.DeleteNodeByKey(10))
        self.assertTrue(self.full_tree.DeleteNodeByKey(14))
        self.assertTrue(self.full_tree.DeleteNodeByKey(12))
        self.find_after_delete = self.full_tree.FindNodeByKey(5)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(1)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(2)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(3)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(6)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(7)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(13)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(12)
        self.assertFalse(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(11)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(14)
        self.assertFalse(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(15)
        self.assertTrue(self.find_after_delete.NodeHasKey)
        self.find_after_delete = self.full_tree.FindNodeByKey(10)
        self.assertFalse(self.find_after_delete.NodeHasKey)
        # Тестируем удаление корня
        self.assertTrue(self.test_tree1.DeleteNodeByKey(5))
        self.find_after_delete = self.test_tree1.FindNodeByKey(5)
        self.assertFalse(self.find_after_delete.NodeHasKey)

    def test_count(self):
        self.assertEqual(self.full_tree.Count(), 15)
        self.assertEqual(self.empty_tree.Count(), 0)
        self.assertEqual(self.test_tree1.Count(), 1)
        self.assertTrue(self.full_tree.DeleteNodeByKey(7))
        self.assertEqual(self.full_tree.Count(), 14)
