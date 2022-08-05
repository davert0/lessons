from unittest import TestCase
from power_set import PowerSet

class TestPowerSet(TestCase):
    def setUp(self) -> None:
        self.set_ = PowerSet()


    def test_put(self):
        self.set_.put('abc')
        self.assertTrue(self.set_.get("abc"))
        self.set_.put('abc')
        self.assertTrue(self.set_.get("abc"))
        self.assertEqual(len(self.set_.slots), 1)

    def test_remove(self):
        self.set_.put('abc')
        self.assertEqual(len(self.set_.slots), 1)
        self.assertEqual(self.set_.remove('abc'), True)
        self.assertFalse(self.set_.get('abc'))

    def test_intersect(self):
        self.set_.put('a')
        self.set_.put('b')
        self.set_.put('c')
        set2 = PowerSet()
        set2.put('d')
        set2.put('e')
        set2.put('b')
        set3 = self.set_.intersection(set2)
        self.assertEqual({'b':'b'}, set3.slots)
        set2.remove('b')
        set3 = self.set_.intersection(set2)
        self.assertEqual({}, set3.slots)


    def test_union(self):
        self.set_.put('a')
        self.set_.put('b')
        self.set_.put('c')
        set2 = PowerSet()
        set2.put('d')
        set2.put('e')
        set2.put('b')
        set3 = self.set_.union(set2)
        self.assertEqual({'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e'}, set3.slots)

    """
    разница difference(), чтобы в результате получались как пустое, так и непустое множества;
    """
    def test_difference(self):
        self.set_.put('a')
        self.set_.put('b')
        self.set_.put('c')
        set2 = PowerSet()
        set2.put('d')
        set2.put('e')
        set2.put('b')
        set3 = self.set_.difference(set2)
        self.assertEqual({'a': 'a', 'c': 'c'}, set3.slots)
        set2.remove('d')
        set2.remove('e')
        # print(self.set_.slots)
        # print(set2.slots)
        set3 = self.set_.intersection(set2)
        self.assertEqual({'a': 'a', 'c': 'c'}, set3.slots)