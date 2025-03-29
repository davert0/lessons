from functools import reduce

lst = [15, 1, 25, 2, 30, 3, 10, 5]


print(
    reduce(
        lambda acc, x: (acc[0] + x[0] * (x[1] - acc[1]), x[1]),
        zip(lst[::2], lst[1::2])
    )[0]
)
