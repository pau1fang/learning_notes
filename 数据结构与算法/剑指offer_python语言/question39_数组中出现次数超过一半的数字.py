def more_than_half_num(arr, length):
    if arr is None or length<=0:
        return 0

    mid = length >> 1
    start = 0
    end = length - 1
    index = partition(arr, length, start, end)

    while index != mid:
        if index > mid:
            index = partition(arr, length, start, index-1)
        else:
            index = partition(arr, length, index+1, end)
    result = arr[mid]
    if not check_more_than_half(arr, result):
        result = 0
    return result


def partition(arr, length, start, end):
    if start >= end:
        return start
    left = start+1
    index = start
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= arr[index]:
            left += 1
        while arr[right] >= arr[index] and left <= right:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[index], arr[right] = arr[right], arr[right]
    return right


def check_more_than_half(arr, val):
    times = 0
    for i in arr:
        if i == val:
            times += 1
    if times * 2 <= len(arr):
        return False
    else:
        return True


def more_than_half_num2(arr, length):
    times = 0
    val = 0
    for i in arr:
        if times == 0:
            val = i
            times = 1
        else:
            if val == i:
                times += 1
            else:
                times -= 1
    result = val
    if not check_more_than_half(arr, result):
        result = 0
    return result


l1 = [1,2,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,6,7,8,9,10,11]
n = more_than_half_num(l1[:-5], len(l1)-5)
print(n)
n2 = more_than_half_num2(l1[:-5], len(l1)-5)
print(n2)
