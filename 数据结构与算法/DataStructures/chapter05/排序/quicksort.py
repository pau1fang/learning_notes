import random


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot = alist[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
    alist[right], alist[first] = alist[first], alist[right]
    print(left, right)
    return right


if __name__ == '__main__':
    def random_list(n):
        return [random.randint(0, 100) for i in range(n)]


    a = [9, 5, 4, 3, 2, 3, 1]
    print(a)
    quick_sort(a)
    print(a)
    b = random_list(20)
    print(b)
    quick_sort(b)
    print(b)
    arr1 = [72, 79, 22, 33, 70, 75, 96, 54, 31, 43]

    print(arr1)
    quick_sort(arr1)
    print(arr1)
