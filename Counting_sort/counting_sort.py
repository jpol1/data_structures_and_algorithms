def counting_sort(arr, k):
    """
    :param arr: array with integers numbers greater or equal 0
    :param k: maximum value from array
    :return: sorted array
    """
    counting_arr = [0]*(k+1)
    n = len(arr)
    res = [0]*n

    for num in arr:
        counting_arr[num] += 1

    for idx in range(1, k+1):
        counting_arr[idx] += counting_arr[idx-1]

    for idx in range(n-1, -1, -1):
        val = arr[idx]
        res[counting_arr[val] - 1] = val
        counting_arr[arr[idx]] -= 1

    return res