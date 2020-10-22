def solution(arr, start, end):
    if not arr or (start>end):
        return False
    i = start
    root = arr[end]
    while arr[i] < root:
        i += 1
    j = i
    for k in range(j, end+1):
        if arr[k] < root:
            return False

    left = True
    if start < i:
        left = solution(arr, start, i-1)
    right = True
    if i < end:
        right = solution(arr, i, end-1)
    return left and right


l1 = [5,7,6,9,11,10,8]
l2 = [7,4,6,5]
print(solution(l1, 0, len(l1)-1))
print(solution(l2, 0, len(l2)-1))
