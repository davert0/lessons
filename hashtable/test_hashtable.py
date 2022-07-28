from unittest import TestCase
from hashtable import HashTable

class TestHashTable(TestCase):
    def setUp(self) -> None:
        self.hashtable = HashTable(17, 3)
        self.hashtable_size_six_step_two = HashTable(6, 2)

    def test_hash_fun(self):
        self.assertEqual(self.hashtable.hash_fun('a'), 12)
        self.assertEqual(self.hashtable.hash_fun('b'), 13)
        self.assertEqual(self.hashtable.hash_fun('c'), 14)
        self.assertEqual(self.hashtable.hash_fun('d'), 15)
        self.assertEqual(self.hashtable.hash_fun('e'), 16)
        self.assertEqual(self.hashtable.hash_fun('f'), 0)
        self.assertEqual(self.hashtable.hash_fun('v'), 16)

    def test_seek_slot_size_17_step_3(self):
        self.assertEqual(self.hashtable.seek_slot('e'), 16)
        self.hashtable.slots[16] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 2)
        self.hashtable.slots[2] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 5)
        self.hashtable.slots[5] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 8)
        self.hashtable.slots[8] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 11)
        self.hashtable.slots[11] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 14)
        self.hashtable.slots[14] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 0)
        self.hashtable.slots[0] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 3)
        self.hashtable.slots[3] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 6)
        self.hashtable.slots[6] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 9)
        self.hashtable.slots[9] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 12)
        self.hashtable.slots[12] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 15)
        self.hashtable.slots[15] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 1)
        self.hashtable.slots[1] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 4)
        self.hashtable.slots[4] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 7)
        self.hashtable.slots[7] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 10)
        self.hashtable.slots[10] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), 13)
        self.hashtable.slots[13] = "e"
        self.assertEqual(self.hashtable.seek_slot('v'), None)

    def test_seek_slot_size_6_step_2(self):
        self.assertEqual(self.hashtable_size_six_step_two.seek_slot('e'), 5)
        self.hashtable_size_six_step_two.slots[5] = "e"
        self.assertEqual(self.hashtable_size_six_step_two.seek_slot('e'), 1)
        self.hashtable_size_six_step_two.slots[1] = "e"
        self.assertEqual(self.hashtable_size_six_step_two.seek_slot('e'), 3)
        self.hashtable_size_six_step_two.slots[3] = "e"
        self.assertEqual(self.hashtable_size_six_step_two.seek_slot('e'), None)


    def test_find(self):
        self.assertEqual(self.hashtable.put("e"), 16)
        self.assertEqual(self.hashtable.find("e"), 16)
        self.assertEqual(self.hashtable.put("v"), 2)
        self.assertEqual(self.hashtable.find("v"), 2)
