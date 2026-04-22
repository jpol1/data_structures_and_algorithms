def selection_sort(arr):
    length = len(arr)
    for i in range(length):

        tmp_min = i
        for m in range(i+1, length):
            if arr[m] < arr[tmp_min]:
                tmp_min = m
        arr[i], arr[tmp_min] = arr[tmp_min], arr[i]

    return arr