
def find_second_max(list_, first_max, second_max):
    if not list_:
        return second_max
    if list_[0] >= first_max:
        second_max = first_max
        first_max = list_[0]
    return find_second_max(list_[1:], first_max, second_max)


def get_second_max(list_: list[int]):
    first_max, second_max = (list_[0], list_[1]) if list_[0] > list_[1] else (list_[1], list_[0])
    return find_second_max(list_[2:], first_max, second_max)
