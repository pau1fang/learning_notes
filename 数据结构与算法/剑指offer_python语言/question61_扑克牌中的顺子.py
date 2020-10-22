def solution(arr):
    arr.sort()
    count_of_0 = 0
    length = len(arr)
    for i in arr:
        if i == 0:
            count_of_0 += 1
    count_of_gap = 0
    small = count_of_0
    big = small + 1
    while big < length:
        if arr[small] == arr[big]:
            return False
        count_of_gap += arr[big] - arr[small] - 1
        small = big
        big += 1
    if count_of_gap > count_of_0:
        return False
    else:
        return True


array = [1,2,3,4,6]
print(solution(array))
