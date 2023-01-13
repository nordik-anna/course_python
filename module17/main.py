from func import sort, is_int, binary_search
import sys

arr = input().split(' ')
if len(arr) == 0:
    print("список пуст")
    sys.exit()

for i in range(len(arr)):
    if not is_int(arr[i]):
        print("invalid input:", arr[i])
        sys.exit()

arr = [int(x) for x in arr]
someInt = int(input())

sort(arr)
findInd = binary_search(arr, someInt)

if findInd >= 0:
    print(f'индекс введенного элемента: {findInd}')
else:
    if someInt > max(arr):
        maxInt = someInt
        i = -1
        while i == -1:
            maxInt -= 1
            i = binary_search(arr, maxInt)
           
        
        print(f'индекс ближайшего большего элемента: {i} со значением: {arr[i]}')
    elif someInt < min(arr):
        minInt = someInt
        i = -1
        while i == -1:
            minInt += 1
            i = binary_search(arr, minInt)
        print(f'индекс ближайшего меньшего элемента: {i} со значением: {arr[i]}')
    
        