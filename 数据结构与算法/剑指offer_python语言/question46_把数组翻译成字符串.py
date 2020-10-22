def solution(num):
    str_num = str(num)
    length = len(str_num)
    result = [1 for _ in range(length + 1)]
    if length == 1:
        return 1
    for i in range(2, length + 1):
        if 10 <= int(str_num[i - 2] + str_num[i - 1]) < 26:
            result[i] = result[i - 1] + result[i - 2]
        else:
            result[i] = result[i - 1]
    print(result)
    return result[length]


def solution2(num):
    str_num = str(num)
    length = len(str_num)
    if length == 1:
        return 1
    a = 1
    b = 1
    for i in range(2, length + 1):
        if 10 <= int(str_num[i - 2] + str_num[i - 1]) < 26:
            b = a+b
            a = b-a
        else:
            a = b
            b = b
    return b


n = 21331331212321312
print(solution(n))
print(solution2(n))
