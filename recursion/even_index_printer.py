from typing import Any


def print_even_index(list_: list[Any]):
    if not list_:
        return
    print(list_[0])
    return print_even_index(list_[2:])
