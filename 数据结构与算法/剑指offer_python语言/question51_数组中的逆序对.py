def solution(arr: list):
    if not arr:
        return 0
    length = len(arr)
    copy = arr.copy()
    count = helper(arr, copy, 0, length - 1)
    return count


def helper(data, copy, start, end):
    if start == end:
        copy[start] = data[start]
        return 0

    mid = (end - start + 1) // 2
    left = helper(copy, data, start, start + mid - 1)
    right = helper(copy, data, start + mid, end)

    i, j = start + mid - 1, end
    index_copy = end
    count = 0
    while i >= start and j >= start + mid:
        if data[i] > data[j]:
            copy[index_copy] = data[i]
            i -= 1
            index_copy -= 1
            count += j - start - mid + 1
        else:
            copy[index_copy] = data[j]
            index_copy -= 1
            j -= 1
    while i >= start:
        copy[index_copy] = data[i]
        i -= 1
        index_copy -= 1
    while j >= start + mid:
        copy[index_copy] = data[j]
        j -= 1
        index_copy -= 1
    return left + right + count


a_list = [7, 5, 6, 4]
print(solution(a_list))
