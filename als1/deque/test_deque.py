from unittest import TestCase
from deque_ import Deque
from palindrome import is_palindrome


class TestQueue(TestCase):
    def setUp(self) -> None:
        self.deque = Deque()

    def test_add_front(self):
        self.deque.addFront(5)
        self.deque.addFront(6)
        self.assertEqual(self.deque.size(), 2)
        self.assertIn(5, self.deque.dequeue)
        self.assertIn(6, self.deque.dequeue)
        self.assertEqual([6, 5], self.deque.dequeue)

    def test_add_tail(self):
        self.deque.addTail(7)
        self.deque.addTail(8)
        self.deque.addTail(9)
        self.assertEqual(self.deque.size(), 3)
        self.assertIn(7, self.deque.dequeue)
        self.assertIn(8, self.deque.dequeue)
        self.assertIn(9, self.deque.dequeue)
        self.assertEqual([7, 8, 9], self.deque.dequeue)

    def test_removeFront(self):
        for i in range(3):
            self.deque.addFront(i)
        self.assertEqual(2, self.deque.removeFront())
        self.assertEqual(2, self.deque.size())
        self.assertEqual(1, self.deque.removeFront())
        self.assertEqual(1, self.deque.size())
        self.assertEqual(0, self.deque.removeFront())
        self.assertEqual(None, self.deque.removeFront())

    def test_removeTail(self):
        for i in range(3):
            self.deque.addFront(i)
        self.assertEqual(0, self.deque.removeTail())
        self.assertEqual(2, self.deque.size())
        self.assertEqual(1, self.deque.removeTail())
        self.assertEqual(1, self.deque.size())
        self.assertEqual(2, self.deque.removeTail())
        self.assertEqual(None, self.deque.removeTail())


class TestIsPalindrome(TestCase):
    def setUp(self) -> None:
        self.palindromes = [
            "Poor Dan is in a droop.",
            "Sit on a potato pan, Otis.",
            "noon",
            "civic",
            "racecar",
            "level",
            "No lemon, no melon",
            "Mr. Owl ate my metal worm.",
        ]

    def test_is_palindrome(self):
        for palindrome in self.palindromes:
            self.assertTrue(is_palindrome(palindrome))
