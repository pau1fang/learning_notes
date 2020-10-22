def solution(arr):
    current_sum = 0
    greatest_sum = float("-inf")
    for i in arr:
        if current_sum <= 0:
            current_sum = i
        else:
            current_sum += i
        if greatest_sum < current_sum:
            greatest_sum = current_sum
    return greatest_sum


def solution2(arr):
    """
    动态规划：f(i)表示以第i个数字结尾的子数组的最大和
    则需要求max[f(i)]其中0<=i<n
    """
    greatest_sum = float("-inf")
    sum_list = [0 for _ in range(len(arr))]
    sum_list[0] = arr[0]
    for i in range(1, len(arr)):
        if sum_list[i - 1] <= 0:
            sum_list[i] = arr[i]
        else:
            sum_list[i] = sum_list[i - 1] + arr[i]
    for i in sum_list:
        if i > greatest_sum:
            greatest_sum = i
    return greatest_sum


def solution3(arr):
    """
    动态规划的精简版，其实与第一种方法一样，
    只是解题思路不同
    """
    greatest_sum = float("-inf")
    current_sum = 0
    for i in arr:
        if current_sum <= 0:
            current_sum = i
        else:
            current_sum += i
        if current_sum > greatest_sum:
            greatest_sum = current_sum
    return greatest_sum


a_list = [1, -2, 3, 10, -4, 7, 2, -5]
res = solution(a_list)
print(res)
print(solution2(a_list))
print(solution3(a_list))
