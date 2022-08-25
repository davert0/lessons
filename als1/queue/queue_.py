class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop()

    def size(self):
        return len(self.queue)
