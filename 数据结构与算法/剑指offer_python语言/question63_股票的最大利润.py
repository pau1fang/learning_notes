def solution(arr):
    left = 0
    right = len(arr)-1
    left_value = float('inf')
    right_value = float("-inf")
    while left < right:
        if arr[left] < left_value:
            left_value = arr[left]
        if arr[right] > right_value:
            right_value = arr[right]
        left += 1
        right -= 1
    return right_value-left_value


def solution2(arr):
    if len(arr) < 2:
        return 0
    min_ = arr[0]
    max_diff = arr[1] - min_
    for i in range(2, len(arr)-1):
        if min_ > arr[i-1]:
            min_ = arr[i-1]
        if arr[i] - min_ > max_diff:
            max_diff = arr[i] - min_

    return max_diff


array = [9,11,8,5,7,12,16,14]
print(solution(array))
print(solution2(array))
