def radix_sort(arr, size):
    exp = 1
    for idx in range(size):
        arr.sort(key=lambda x: (x//exp)%10)
        exp *= 10
    return arr