import unittest


from linked_list import Node, LinkedList
from sum_lists import sum_linked_lists


class TestDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_list = LinkedList()

        self.full_list = LinkedList()
        for i in range(100):
            self.full_list.add_in_tail(Node(i))

    def test_delete_one_with_empty_list(self):
        self.assertEqual(self.empty_list.delete(24), None)
        self.assertEqual(self.empty_list.len(), 0)

    def test_delete_one_with_full_list_from_middle(self):
        self.assertEqual(self.full_list.find(24).value, 24)
        self.assertEqual(self.full_list.len(), 100)
        self.full_list.delete(24)
        self.assertEqual(self.full_list.find(24), None)
        self.assertEqual(self.full_list.find(23).next, self.full_list.find(25))
        self.assertEqual(self.full_list.len(), 99)
        self.assertEqual(self.full_list.head.value, 0)
        self.assertEqual(self.full_list.tail.value, 99)

    def test_delete_one_with_full_list_from_beginning(self):
        self.assertEqual(self.full_list.find(0).value, 0)
        self.assertEqual(self.full_list.len(), 100)
        self.full_list.delete(0)
        self.assertEqual(self.full_list.find(0), None)
        self.assertEqual(self.full_list.find(1).next, self.full_list.find(2))
        self.assertEqual(self.full_list.len(), 99)
        self.assertEqual(self.full_list.head.value, 1)
        self.assertEqual(self.full_list.tail.value, 99)

    def test_delete_one_with_full_list_from_end(self):
        self.assertEqual(self.full_list.find(99).value, 99)
        self.assertEqual(self.full_list.len(), 100)
        self.full_list.delete(99)
        self.assertEqual(self.full_list.find(99), None)
        self.assertEqual(self.full_list.find(98).next, None)
        self.assertEqual(self.full_list.len(), 99)
        self.assertEqual(self.full_list.head.value, 0)
        self.assertEqual(self.full_list.tail.value, 98)

    def test_delete_one_from_one_item_list(self):
        self.empty_list.add_in_tail(Node(5))
        self.empty_list.delete(5)
        self.assertEqual(self.empty_list.len(), 0)
        self.assertEqual(self.empty_list.head, None)
        self.assertEqual(self.empty_list.tail, None)

    def test_add_to_end_same_values_and_delete_one(self):
        for i in range(5):
            self.full_list.add_in_tail(Node(99))
        self.assertEqual(self.full_list.len(), 105)
        first_99 = self.full_list.find(99)

        self.full_list.delete(99)
        self.assertEqual(self.full_list.len(), 104)
        second_99 = self.full_list.find(99)
        self.assertNotEqual(
            self.full_list.find(98).next,
            first_99,
        )
        self.assertEqual(
            self.full_list.find(98).next,
            second_99,
        )

    def test_delete_all_from_beginning(self):
        for i in range(6):
            self.empty_list.add_in_tail(Node(1))
        self.empty_list.add_in_tail(Node(6))
        for i in range(3):
            self.empty_list.add_in_tail(Node(7))
        self.assertEqual(self.empty_list.len(), 10)
        self.empty_list.delete(1, all=True)
        self.assertEqual(self.empty_list.len(), 4)
        self.assertEqual(self.empty_list.find(1), None)
        self.assertEqual(self.empty_list.head.value, 6)

    def test_delete_all_from_beginning(self):
        for i in range(6):
            self.empty_list.add_in_tail(Node(1))
        self.empty_list.add_in_tail(Node(6))
        for i in range(3):
            self.empty_list.add_in_tail(Node(7))
        self.empty_list.delete(1, all=True)
        self.assertEqual(self.empty_list.len(), 4)
        self.assertEqual(self.empty_list.find(1), None)
        self.assertEqual(self.empty_list.head.value, 6)
        self.assertEqual(self.empty_list.tail.value, 7)

    def test_delete_all_in_middle(self):
        self.empty_list.add_in_tail(Node(1))
        for i in range(5):
            self.empty_list.add_in_tail(Node(6))
        for i in range(3):
            self.empty_list.add_in_tail(Node(7))
        self.assertEqual(self.empty_list.len(), 9)

        self.empty_list.delete(6, all=True)
        self.assertEqual(self.empty_list.len(), 4)
        self.assertEqual(self.empty_list.find(6), None)
        self.assertEqual(self.empty_list.head.value, 1)
        self.assertEqual(self.empty_list.tail.value, 7)

    def test_delete_all_in_end(self):
        self.empty_list.add_in_tail(Node(1))
        for i in range(5):
            self.empty_list.add_in_tail(Node(6))
        for i in range(3):
            self.empty_list.add_in_tail(Node(7))
        self.assertEqual(self.empty_list.len(), 9)

        self.empty_list.delete(7, all=True)
        self.assertEqual(self.empty_list.len(), 6)
        self.assertEqual(self.empty_list.find(7), None)
        self.assertEqual(self.empty_list.head.value, 1)
        self.assertEqual(self.empty_list.tail.value, 6)

    def test_delete_all_in_everyplace(self):
        for i in range(2):
            self.empty_list.add_in_tail(Node(4))
        self.empty_list.add_in_tail(Node(1))
        for i in range(5):
            self.empty_list.add_in_tail(Node(6))
        for i in range(2):
            self.empty_list.add_in_tail(Node(4))
        for i in range(3):
            self.empty_list.add_in_tail(Node(7))
        for i in range(2):
            self.empty_list.add_in_tail(Node(4))
        self.assertEqual(self.empty_list.len(), 15)
        self.empty_list.delete(4, all=True)
        self.assertEqual(self.empty_list.len(), 9)
        self.assertEqual(self.empty_list.find(4), None)
        self.assertEqual(self.empty_list.head.value, 1)
        self.assertEqual(self.empty_list.tail.value, 7)

    def test_delete_all_to_empty(self):
        for i in range(5):
            self.empty_list.add_in_tail(Node(6))
        self.assertEqual(self.empty_list.len(), 5)
        self.empty_list.delete(6, all=True)
        self.assertEqual(self.empty_list.len(), 0)
        self.assertEqual(self.empty_list.head, None)
        self.assertEqual(self.empty_list.tail, None)


class TestInsert(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()

    def test_insert_to_empty_list(self):
        node_1 = Node(14)
        self.list_.insert(None, node_1)
        self.assertEqual(self.list_.len(), 1)
        self.assertEqual(self.list_.head, node_1)
        self.assertEqual(self.list_.tail, node_1)
        node_2 = Node(15)
        self.list_.insert(None, node_2)
        self.assertEqual(self.list_.len(), 2)
        self.assertEqual(self.list_.head, node_2)
        self.assertEqual(self.list_.tail, node_1)
        self.assertEqual(node_2.next, node_1)
        node_3 = Node(16)
        self.list_.insert(node_1, node_3)
        self.assertEqual(self.list_.len(), 3)
        self.assertEqual(self.list_.head, node_2)
        self.assertEqual(self.list_.tail, node_3)
        self.assertEqual(node_1.next, node_3)
        self.list_.insert(node_1, Node(19))
        self.assertEqual(self.list_.len(), 4)
        self.assertEqual(self.list_.head, node_2)
        self.assertEqual(self.list_.tail.value, 16)
        self.assertEqual(node_1.next.value, 19)


class TestLen(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_list = LinkedList()

        self.full_list = LinkedList()
        for i in range(100):
            self.full_list.add_in_tail(Node(i))

    def test_empty_len(self):
        self.assertEqual(self.empty_list.len(), 0)

    def test_full_len(self):
        self.assertEqual(self.full_list.len(), 100)


class TestFindAll(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_list = LinkedList()

        self.full_list = LinkedList()
        for i in range(100):
            self.full_list.add_in_tail(Node(i))

    def test_find_all_empty_list(self):
        self.assertEqual(self.empty_list.find_all(12), [])

    def test_find_all_one_value(self):
        self.assertEqual(len(self.full_list.find_all(1)), 1)

    def test_find_all_several_values(self):
        for i in range(5):
            self.full_list.add_in_tail(Node(5))
        self.assertEqual(len(self.full_list.find_all(5)), 6)


class TestClean(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_list = LinkedList()

        self.full_list = LinkedList()
        for i in range(100):
            self.full_list.add_in_tail(Node(i))

    def test_clean_empty(self):
        self.empty_list.clean()
        self.assertEqual(self.empty_list.head, None)
        self.assertEqual(self.empty_list.tail, None)

    def test_clean_full(self):
        self.full_list.clean()
        self.assertEqual(self.full_list.head, None)
        self.assertEqual(self.full_list.tail, None)
        self.assertEqual(self.full_list.len(), 0)


class TestSumLists(unittest.TestCase):
    def setUp(self) -> None:
        self.first_list = LinkedList()
        self.second_list = LinkedList()

        for i in range(5):
            self.first_list.add_in_tail(Node(i))
            self.second_list.add_in_tail(Node(i))

    def test_sum(self):
        res = sum_linked_lists(self.first_list, self.second_list)
        self.assertEqual(res, [0, 2, 4, 6, 8])
