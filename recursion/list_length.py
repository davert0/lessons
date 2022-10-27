def get_list_length(list_: list):
    if len(list_) == 0:
        return 0
    list_.pop(0)
    return 1 + get_list_length(list_)


def get_list_length_try_except(list_: list):
    try:
        list_.pop(0)
    except IndexError:
        return 0
    return 1 + get_list_length_try_except(list_)
