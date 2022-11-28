def GenerateBBSTArray(a):
    a = sorted(a)
    res = [None] * len(a)
    middle = len(a)//2
    index = 0
    res[index] = a[middle]
    queue = [a[middle:], a[:middle]]
    index +=1 
    while index < len(res):
        sub_arr = queue.pop()
        middle = len(sub_arr)//2
        res[index] = sub_arr[middle]
        queue.insert(0, sub_arr[:middle])
        queue.insert(0, sub_arr[middle:])
        index += 1

    return res