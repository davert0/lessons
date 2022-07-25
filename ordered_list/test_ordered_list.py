from unittest import TestCase
from ordered_list import OrderedList

# 6. Добавьте тесты для добавления, удаления и поиска элемента по его значению -- каждый случай с учётом признака упорядоченности.


class TestOrderedList(TestCase):
    def setUp(self) -> None:
        self.list = OrderedList(asc=True)
        self.list_desc = OrderedList(asc=False)

    # add_empty
    def test_add_to_empty_list(self):
        self.list.add(5)
        self.assertEqual(self.list.head.value, 5)
        self.assertEqual(self.list.head.next, None)
        self.assertEqual(self.list.tail.value, 5)

    # add_asc
    def test_add_smaller_value_to_list_with_one_element_asc(self):
        self.list.add(7)
        self.list.add(3)
        self.assertEqual(self.list.tail.value, 7)
        self.assertEqual(self.list.tail.prev.value, 3)
        self.assertEqual(self.list.tail.next, None)
        self.assertEqual(self.list.head.value, 3)
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(self.list.head.next.value, 7)

    def test_add_bigger_value_to_list_with_one_element_asc(self):
        self.list.add(3)
        self.list.add(7)
        self.assertEqual(self.list.tail.value, 7)
        self.assertEqual(self.list.tail.prev.value, 3)
        self.assertEqual(self.list.tail.next, None)
        self.assertEqual(self.list.head.value, 3)
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(self.list.head.next.value, 7)

    def test_add_value_to_middle_filled_list_asc(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.list.add(7)
        self.list.add(8)
        self.list.add(9)
        self.list.add(4)
        self.assertEqual(self.list.len(), 7)
        self.assertEqual(self.list.find(3).next.value, 4)
        self.assertEqual(self.list.find(4).prev.value, 3)
        self.assertEqual(self.list.find(4).next.value, 7)

    def test_add_value_to_start_filled_list_asc(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.list.add(7)
        self.list.add(8)
        self.list.add(9)
        self.list.add(0)
        self.assertEqual(self.list.len(), 7)
        self.assertEqual(self.list.head.value, 0)
        self.assertEqual(self.list.head.next.value, 1)
        self.assertEqual(self.list.head.next.prev.value, 0)

    def test_add_value_to_end_filled_list_asc(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.list.add(7)
        self.list.add(8)
        self.list.add(9)
        self.list.add(10)
        self.assertEqual(self.list.len(), 7)
        self.assertEqual(self.list.tail.value, 10)
        self.assertEqual(self.list.tail.prev.value, 9)
        self.assertEqual(self.list.tail.prev.next.value, 10)

    # add desc
    def test_add_smaller_value_to_list_with_one_element_desc(self):
        self.list_desc.add(7)
        self.list_desc.add(3)
        self.assertEqual(self.list_desc.tail.value, 3)
        self.assertEqual(self.list_desc.tail.prev.value, 7)
        self.assertEqual(self.list_desc.tail.next, None)
        self.assertEqual(self.list_desc.head.value, 7)
        self.assertEqual(self.list_desc.head.prev, None)
        self.assertEqual(self.list_desc.head.next.value, 3)

    def test_add_bigger_value_to_list_with_one_element_desc(self):
        self.list_desc.add(3)
        self.list_desc.add(7)
        self.assertEqual(self.list_desc.tail.value, 3)
        self.assertEqual(self.list_desc.tail.prev.value, 7)
        self.assertEqual(self.list_desc.tail.next, None)
        self.assertEqual(self.list_desc.head.value, 7)
        self.assertEqual(self.list_desc.head.prev, None)
        self.assertEqual(self.list_desc.head.next.value, 3)

    def test_add_value_to_middle_filled_list_desc(self):
        self.list_desc.add(1)
        self.list_desc.add(2)
        self.list_desc.add(3)
        self.list_desc.add(7)
        self.list_desc.add(8)
        self.list_desc.add(9)
        self.list_desc.add(4)
        self.assertEqual(self.list_desc.len(), 7)
        self.assertEqual(self.list_desc.find(3).next.value, 2)
        self.assertEqual(self.list_desc.find(4).prev.value, 7)
        self.assertEqual(self.list_desc.find(4).next.value, 3)
        self.assertEqual(self.list_desc.head.value, 9)

    def test_add_value_to_end_filled_list_desc(self):
        self.list_desc.add(1)
        self.list_desc.add(2)
        self.list_desc.add(3)
        self.list_desc.add(7)
        self.list_desc.add(8)
        self.list_desc.add(9)
        self.list_desc.add(0)
        self.assertEqual(self.list_desc.len(), 7)
        self.assertEqual(self.list_desc.head.value, 9)
        self.assertEqual(self.list_desc.head.next.value, 8)
        self.assertEqual(self.list_desc.head.next.prev.value, 9)
        self.assertEqual(self.list_desc.tail.value, 0)
        self.assertEqual(self.list_desc.tail.prev.value, 1)

    def test_add_value_to_start_filled_list_desc(self):
        self.list_desc.add(1)
        self.list_desc.add(2)
        self.list_desc.add(3)
        self.list_desc.add(7)
        self.list_desc.add(8)
        self.list_desc.add(9)
        self.list_desc.add(10)
        self.assertEqual(self.list_desc.len(), 7)
        self.assertEqual(self.list_desc.head.value, 10)
        self.assertEqual(self.list_desc.head.next.value, 9)


    # delete_from_empty
    def test_delete_value_from_empty_list(self):
        self.assertEqual(self.list.delete(5), None)

    def test_delete_from_end_asc(self):
        self.list.add(7)
        self.list.add(3)
        self.list.delete(7)
        self.assertEqual(self.list.len(), 1)
        self.assertEqual(self.list.head.value, 3)
        self.assertEqual(self.list.tail.value, 3)
        self.assertEqual(self.list.head.next, None)
        self.assertEqual(self.list.find(7), None)

    def test_delete_from_start_asc(self):
        self.list.add(7)
        self.list.add(3)
        self.list.delete(3)
        self.assertEqual(self.list.len(), 1)
        self.assertEqual(self.list.head.value, 7)
        self.assertEqual(self.list.tail.value, 7)
        self.assertEqual(self.list.head.next, None)
        self.assertEqual(self.list.find(3), None)


    def test_delete_from_end_desc(self):
        self.list_desc.add(7)
        self.list_desc.add(3)
        self.list_desc.delete(3)
        self.assertEqual(self.list_desc.len(), 1)
        self.assertEqual(self.list_desc.head.value, 7)
        self.assertEqual(self.list_desc.tail.value, 7)
        self.assertEqual(self.list_desc.head.next, None)
        self.assertEqual(self.list.find(3), None)


    def test_delete_from_start_desc(self):
        self.list_desc.add(7)
        self.list_desc.add(3)
        self.list_desc.delete(7)
        self.assertEqual(self.list_desc.len(), 1)
        self.assertEqual(self.list_desc.head.value, 3)
        self.assertEqual(self.list_desc.tail.value, 3)
        self.assertEqual(self.list_desc.head.next, None)
        self.assertEqual(self.list.find(7), None)


    def test_delete_from_middle_asc(self):
        for i in range(6):
            self.list.add(i)

        self.list.delete(4)
        self.assertEqual(self.list.len(), 5)
        self.assertEqual(self.list.find(3).next.value, 5)
        self.assertEqual(self.list.find(5).prev.value, 3)
        self.assertEqual(self.list.find(4), None)


    def test_delete_from_middle_desc(self):
        for i in range(6):
            self.list_desc.add(i)

        self.list_desc.delete(4)
        self.assertEqual(self.list_desc.len(), 5)
        self.assertEqual(self.list_desc.find(3).next.value, 2)
        self.assertEqual(self.list_desc.find(5).prev, None)
        self.assertEqual(self.list_desc.find(5).next.value, 3)
        self.assertEqual(self.list_desc.find(3).prev.value, 5)
        self.assertEqual(self.list_desc.find(4), None)

