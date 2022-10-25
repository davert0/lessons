def exponentiate(n, m, res=None):
    if m == 0:
        return 1
    if m == 1:
        return n
    if res is None:
        res = n * n
    else:
        res = res * n
    if m == 2:
        return res
    return exponentiate(n, m-1, res=res)