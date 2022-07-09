from attr import s
from stack import Stack

def check_brackets_balance(brackets: str):
    stack = Stack()
    for bracket in brackets:
        if bracket == "(":
            stack.push(bracket)
        elif stack.peek() == "(":
            stack.pop()
    return stack.size() == 0
