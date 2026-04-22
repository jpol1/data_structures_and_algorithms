def lomuto_partition(arr, p, r):
    pivot = arr[r]
    i = p-1
    j = p
    while (j!=r):
        if (arr[j] < pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
        j+=1

    arr[i+1], arr[j] = arr[j], arr[i+1]

    return i+1