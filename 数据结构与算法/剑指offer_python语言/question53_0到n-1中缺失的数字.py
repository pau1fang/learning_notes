def solution(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid != arr[mid]:
            if mid == 0 or arr[mid-1] == mid - 1:
                return mid
            right = mid - 1
        else:
            left = mid + 1

    return left


array = [0]
print(solution(array))
