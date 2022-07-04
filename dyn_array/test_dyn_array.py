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
        

        