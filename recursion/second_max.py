def get_second_max(list_: list[int]):
    def find_second_max(index, first_max, second_max):
        if len(list_) == index:
            return second_max
        if list_[index] >= first_max:
            second_max = first_max
            first_max = list_[index]
        elif list_[index] > second_max:
            second_max = list_[index]
        
        return find_second_max(index + 1, first_max, second_max)

    first_max, second_max = (
        (list_[0], list_[1]) if list_[0] > list_[1] else (list_[1], list_[0])
    )

    return find_second_max(2, first_max, second_max)
