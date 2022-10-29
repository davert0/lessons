def get_list_length(list_: list):
    if len(list_) == 0:
        return 0
    list_.pop(0)
    return 1 + get_list_length(list_)
