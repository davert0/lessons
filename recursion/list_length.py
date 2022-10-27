def get_list_length(list_: list, res=0):
    try:
        list_.pop(0)
        res += 1
    except IndexError:
        ...
