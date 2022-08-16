from deque_ import Deque
import string


def is_palindrome(text: str):
    text = (
        text.lower()
        .replace(" ", "")
        .translate(str.maketrans("", "", string.punctuation))
    )

    deque_front = Deque()
    deque_back = Deque()
    front = []
    back = []
    for letter in text:
        deque_front.addTail(letter)
    deque_back.dequeue = deque_front.dequeue.copy()

    while deque_front.size() > 0:
        front.append(deque_front.removeFront())

    while deque_back.size() > 0:
        back.append(deque_back.removeTail())

    return back == front
