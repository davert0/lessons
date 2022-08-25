from unittest import TestCase
from native_cache import NativeCache


class TestNativeDict(TestCase):
    def setUp(self):
        self.native_cache = NativeCache(5)

    def test_put_and_override(self):
        self.native_cache.put("foo", "bar")
        self.assertEqual(self.native_cache.get("foo"), "bar")
        self.native_cache.put("foo", "baz")
        self.assertEqual(self.native_cache.get("foo"), "baz")
        self.assertEqual(self.native_cache.get("bar"), None)
        self.native_cache.put("1", "2")
        self.native_cache.put("3", "4")
        self.native_cache.put("5", "6")
        self.native_cache.put("6", "7")
        self.assertEqual(self.native_cache.get("3"), "4")
        self.assertEqual(self.native_cache.get("5"), "6")
        self.assertEqual(self.native_cache.get("6"), "7")
        self.native_cache.put("6", "9")
        self.assertEqual(self.native_cache.get("6"), "9")
        self.assertEqual(self.native_cache.get("6"), "9")
        self.assertEqual(self.native_cache.get("6"), "9")
        self.native_cache.put("7", "8")
        self.assertEqual(self.native_cache.get("1"), None)
        self.assertEqual(self.native_cache.get("7"), "8")
