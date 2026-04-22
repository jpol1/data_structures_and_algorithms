def bubblesort(arr):
    arr_size = len(arr)

    for i in range(arr_size):
        flag = True

        for j in range(arr_size-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False

        if (flag):
            break