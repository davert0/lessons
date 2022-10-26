def recursive_sum(n: int):
    n = str(n)
    if len(n) == 1:
        return int(n)
    return int(n[:1]) + recursive_sum(int(n[1:]))
