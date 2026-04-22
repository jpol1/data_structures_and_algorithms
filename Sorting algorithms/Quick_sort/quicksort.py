from hoare_partition import hoare_partition
from lomuto_partition import lomuto_partition

def quicksort_hoare(arr, p, r, step):
    if p < r:
        q = hoare_partition(arr, p, r)
        quicksort_hoare(arr, p, q, step)
        quicksort_hoare(arr, q+1, r, step)

def quicksort_lomuto(arr, p, r):
    if p < r:
        q = lomuto_partition(arr, p , r)
        quicksort_lomuto(arr, p, q-1)
        quicksort_lomuto(arr, q+1, r)