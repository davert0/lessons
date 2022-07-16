from unittest import TestCase
from queue_ import Queue

class TestQueue(TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_queue(self):
        for i in range(3):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.size(), 0)
