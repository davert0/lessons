def recursive_sum(n: int, res=None):
    n = str(n)
    if not res:
        res = 0 + int(n[0])
    else:
        res += int(n[0])
    n = n[1:]
    if len(n) == 0:
        return res
    return recursive_sum(int(n), res)