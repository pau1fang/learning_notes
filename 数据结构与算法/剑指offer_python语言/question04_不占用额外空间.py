def solution(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        return -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = ((end - start) >> 1) + start  # 位运算符优先级比+低，因此需用括号
        count = count_range(arr, start, mid)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > mid - start + 1:
            end = mid
        else:
            start = mid + 1
    return -1


def count_range(arr_, start_, end_):
    count_ = 0
    for i in arr_:
        if start_ <= i <= end_:
            count_ += 1
    return count_


l1 = [1, 2, 3, 4, 5, 6, 0]
l2 = [1, 2, 3, 4, 4, 5, 3]
l3 = []

arr = [l1, l2, l3]

for i in arr:
    res = solution(i)
    print(res)
