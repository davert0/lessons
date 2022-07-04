from unittest import TestCase
from dyn_array import DynArray

class TestInsert(TestCase):
    def setUp(self) -> None:
        self.arr = DynArray()

    def test_insert_buff_not_exceed(self):
        for i in range(5):
            self.arr.append(i)
        self.assertEqual(len(self.arr), 5)
        self.assertEqual(self.arr[4], 4)
        self.arr.insert(4, 6)
        self.assertEqual(len(self.arr), 6)
        self.assertEqual(self.arr[4], 6)
        self.assertEqual(self.arr[5], 4)
        self.assertEqual(self.arr.capacity, 16)


    def test_insert_buff_exceed(self):
        for i in range(16):
            self.arr.append(i)
        self.assertEqual(len(self.arr), 16)
        self.assertEqual(self.arr.capacity, 16)
        self.assertEqual(self.arr[15], 15)
        self.arr.insert(4, 6)
        self.assertEqual(len(self.arr), 17)
        self.assertEqual(self.arr[4], 6)
        self.assertEqual(self.arr[5], 4)
        self.assertEqual(self.arr[15], 14)
        self.assertEqual(self.arr.capacity, 32)

    def test_unnexceptable_position(self):
        for i in range(5):
            self.arr.append(i)
        self.assertEqual(len(self.arr), 5)
        self.assertEqual(self.arr[4], 4)
        self.arr.insert(5,6)
        self.assertEqual(len(self.arr), 6)
        self.assertEqual(self.arr[5], 6)
        self.assertRaises(IndexError, self.arr.insert, 7, 6)
        

class TestDelete(TestCase):
    def setUp(self) -> None:
        self.arr = DynArray()
        for i in range(5):
            self.arr.append(i)


    def test_delete_same_buff(self):
        self.arr.delete(3)
        self.assertEqual(len(self.arr), 4)
        self.assertEqual(self.arr[3], 4)
        self.assertEqual(self.arr[2], 2)
        self.assertEqual(self.arr.capacity, 16)

    def test_delete_change_buff(self):
        for i in range(5, 17):
            self.arr.append(i)
        self.assertEqual(len(self.arr), 17)
        self.assertEqual(self.arr.capacity, 32)
        self.arr.delete(16)
        self.assertEqual(self.arr.capacity, 32)
        self.arr.delete(15)
        self.assertEqual(self.arr.capacity, int(32/1.5))

    def test_delete_unsupported_index(self):
        self.assertRaises(IndexError, self.arr.delete, 7)

    