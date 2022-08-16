from attr import s
from stack import Stack


def check_brackets_balance(brackets: str):
    stack = Stack()

    if not brackets:
        return None

    for bracket in brackets:
        if bracket == "(":
            stack.push(bracket)
        elif stack.peek() == "(":
            stack.pop()
        else:
            stack.push(bracket)
    return stack.size() == 0
