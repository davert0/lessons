def exponentiate(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * exponentiate(n, m - 1)
