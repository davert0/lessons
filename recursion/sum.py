def recursive_sum(n: int):
    if n < 10:
        return n % 10
    return n % 10 + recursive_sum(n//10)
