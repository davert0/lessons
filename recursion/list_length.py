def get_list_length(list_: list):
    try:
        list_.pop(0)
    except IndexError:
        return 0
    return 1 + get_list_length(list_)
