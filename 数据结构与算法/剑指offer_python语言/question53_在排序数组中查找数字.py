def get_first_k(arr, length, start, end, k):
    if start == 0 and arr[start] == k:
        return 0
    if start == end:
        if arr[start] == k:
            return start
        else:
            return -1

    mid = (end + start) // 2
    if arr[mid] == k and arr[mid - 1] != k:
        return mid
    if k <= arr[mid]:
        return get_first_k(arr, length, start, mid - 1, k)
    else:
        return get_first_k(arr, length, mid + 1, end, k)


def get_last_k(arr, length, start, end, k):
    if end == length - 1 and arr[end] == k:
        return end
    if start == end:
        if arr[end] == k:
            return end
        else:
            return -1

    mid = (end + start) // 2
    if arr[mid] == k and arr[mid + 1] != k:
        return mid
    if arr[mid] <= k:
        return get_last_k(arr, length, mid + 1, end, k)
    else:
        return get_last_k(arr, length, start, mid - 1, k)


def solution(arr, k):
    length = len(arr)
    number = 0
    if length > 0:
        first = get_first_k(arr, length, 0, length - 1, k)
        last = get_last_k(arr, length, 0, length - 1, k)
        if first > -1 and last > -1:
            number = last - first + 1
    return number


def get_first_k2(arr, length, start, end, k):
    if start > end:
        return -1
    mid = (start + end) // 2
    mid_data = arr[mid]
    if mid_data == k:
        if (mid > 0 and arr[mid - 1] != k) or mid == 0:
            return mid
        else:
            end = mid - 1
    elif mid_data > k:
        end = mid - 1
    else:
        start = mid + 1
    return get_first_k2(arr, length, k, start, end)


a_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(solution(a_list, 3))
