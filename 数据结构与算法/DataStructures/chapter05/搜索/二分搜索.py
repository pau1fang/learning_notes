def binary_sort(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first < last and not found:
        mid_point = (first+ last)//2
        if alist[mid_point] == item:
            found = True
        else:
            if alist[mid_point]>item:
                last = mid_point-1
            else:
                first = mid_point+1
    return found


def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid_point = len(alist)//2
        if alist[mid_point] == item:
            return True
        else:
            if alist[mid_point] > item:
                return binary_search(alist[:mid_point], item)
            else:
                return binary_search(alist[mid_point+1:], item)


def binary_search3(alist, item):
    return binary_search3_helper(alist, 0, len(alist)-1, item)


def binary_search3_helper(alist, left, right, item):
    if left > right:
        return False
    else:
        mid = (left+right)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid]>item:
                return binary_search3_helper(alist, left, mid-1, item)
            else:
                return binary_search3_helper(alist, mid+1, right, item)
# print(binary_search3(list(range(10)), 9))
