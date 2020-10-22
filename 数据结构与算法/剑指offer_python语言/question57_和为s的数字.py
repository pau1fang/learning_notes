def solution(arr, s):
    small = 0
    big = find_big(arr, s)
    # big = len(arr) - 1
    while small < big:
        sum_ = arr[small] + arr[big]
        if sum_ == s:
            return arr[small], arr[big]
        if sum_ > s:
            big -= 1
        else:
            small += 1
    return -1


def find_big(arr, s):
    if arr[-1] <= s:
        return len(arr) - 1
    start = 0
    end = len(arr) - 2
    mid = (start + end) // 2
    while start < end:
        if arr[mid] <= s < arr[mid + 1]:
            return mid
        if arr[mid] < s:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return start


array = [1,2,4,7,11,15,16,17,20,23]
print(solution(array, 15))

"""
题目二：和为s的连续正数序列
"""


def find_continuous_sequence(sum_):
    if sum_ < 3:
        return
    start = 1
    end = 2
    current_sum = start + end
    while start <= sum_//2:
        if current_sum == sum_:
            for i in range(start, end + 1):
                print(i, end=' ')
            print()
            end += 1
            current_sum += end
        elif current_sum<sum_:
            end += 1
            current_sum += end
        else:
            current_sum -= start
            start += 1


def find_continuous_sequence2(sum_):
    if sum_ < 3:
        return
    small = 1
    big = 2
    middle = (sum_ + 1)//2
    cur_sum = small + big
    while small < middle:
        if cur_sum == sum_:
            for i in range(small, big+1):
                print(i, end=' ')
            print()
        while cur_sum > sum_ and small < middle:
            cur_sum -= small
            small += 1
            if cur_sum == sum_:
                for i in range(small, big+1):
                    print(i, end=' ')
                print()
        big+= 1
        cur_sum += big


for i in range(100):
    find_continuous_sequence2(i)
    print("*"*20)
