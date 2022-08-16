from unittest import TestCase

from stack import Stack


class TestPop(TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
        for i in range(5):
            self.stack.push(i)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.size(), 4)
        for i in range(4):
            self.stack.pop()
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.pop(), None)

    def test_push(self):
        self.stack.push(5)
        self.assertEqual(self.stack.size(), 6)
        self.assertEqual(self.stack.pop(), 5)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 4)
        self.assertEqual(self.stack.size(), 5)
        for i in range(5):
            self.stack.pop()
        self.assertEqual(self.stack.peek(), None)
