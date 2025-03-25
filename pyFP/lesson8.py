from functools import reduce

def second_max(numbers):
    
    result = reduce(
        lambda acc, x: (
            (x, acc[0]) if x >= acc[0] else 
            (acc[0], x) if acc[1] is None or x > acc[1] else 
            acc
        ),
        numbers[1:],  
        (numbers[0], None) 
    )

    if result[1] is None:
        return result[0]
    
    return result[1]


print(second_max([[5, 4, 3, 2, 5]]))