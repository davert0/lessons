class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if not self.stack_1:
            return None
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        res = self.stack_2.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return res

    def size(self):
        return len(self.stack_1)
