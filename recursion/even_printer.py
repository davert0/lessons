def print_even(list_: list[int]):
    if not list_:
        return
    number = list_.pop()
    if number % 2 == 0:
        print(number)
    print_even(list_)
