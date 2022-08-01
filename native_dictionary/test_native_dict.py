from unittest import TestCase
from native_dict import NativeDictionary

class TestNativeDict(TestCase):
    def setUp(self):
        self.native_dict = NativeDictionary(15)

    def test_put_and_override(self):
        self.native_dict.put("foo", "bar")
        self.assertEqual(self.native_dict.get("foo"), "bar")
        self.native_dict.put("foo", "baz")
        self.assertEqual(self.native_dict.get("foo"), "baz")
        self.assertEqual(self.native_dict.get("bar"), None)
    
    def test_is_key(self):
        self.native_dict.put("foo", "bar")
        self.assertTrue(self.native_dict.is_key("foo"))
        self.assertFalse(self.native_dict.is_key("bar"))