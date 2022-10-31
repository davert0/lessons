
def get_max(list_: list[int]):
    if len(list_) == 1:
        return list_[0]
    max_value = get_max(list_[1:])
    return max_value if max_value > list_[0] else list_[0]


def get_second_max(list_: list[int]):
    first_max = get_max(list_)
    list_.remove(first_max)
    return get_max(list_)
