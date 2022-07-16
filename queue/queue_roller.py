from queue_ import Queue
import time

def roll_queue(n: int):
    queue = Queue()

    for i in range(n):
        queue.enqueue(i)

    while True:
        queue.enqueue(queue.dequeue())

