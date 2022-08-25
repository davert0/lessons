from deque_ import Deque
import string


def is_palindrome(text: str):
    prepared_text = (
        text.lower()
        .replace(" ", "")
        .translate(str.maketrans("", "", string.punctuation))
    )

    deque_front = Deque()
    deque_back = Deque()
    front_reading = []
    back_reading = []
    for letter in prepared_text:
        deque_front.addTail(letter)
    deque_back.dequeue = deque_front.dequeue.copy()

    while deque_front.size() > 0:
        front_reading.append(deque_front.removeFront())

    while deque_back.size() > 0:
        back_reading.append(deque_back.removeTail())

    return back_reading == front_reading
