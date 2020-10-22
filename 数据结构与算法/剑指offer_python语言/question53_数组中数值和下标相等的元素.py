def solution(arr):
    if arr is None:
        return
    left = 0
    right = len(arr)-1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == middle:
            return middle
        if arr[middle] < middle:
            left = middle + 1
        else:
            right = middle - 1
    return -1