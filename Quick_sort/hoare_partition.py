def hoare_partition(arr, p, r):
    pivot = arr[p]
    i = p-1
    j = r+1

    while True:

        j -= 1
        while(arr[j] > pivot):
            j -= 1


        i+=1
        while(arr[i] < pivot):
            i += 1

        if (i>=j):
            return j
        arr[i], arr[j] = arr[j], arr[i]