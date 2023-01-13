import random

def sort(nums):
    start = 0
    end = len(nums)-1
    quicksort(nums, start, end)

def quicksort(A, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j: 
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1 
                quicksort(A, l, j)
                quicksort(A, i, r)

def binary_search(elems, elem):
    if len(elems) == 1:
        return 0
    start=0
    end=len(elems)-1

    while start <= end:
        mid = (start + end) // 2
        if elems[mid] == elem:
            return mid
        elif elems[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

def is_int(i):
    return str.isnumeric(i)