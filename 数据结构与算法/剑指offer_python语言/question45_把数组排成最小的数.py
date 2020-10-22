from functools import cmp_to_key


def compare(num1, num2):
    str1 = str(num1)+str(num2)
    str2 = str(num2)+str(num1)
    length = len(str1)
    for i in range(length-1):
        if int(str1[i]) > int(str2[i]):
            return 1
        elif int(str1[i]) < int(str2[i]):
            return -1
    return 0


def solution(arr):
    new_list = arr[:]
    new_list.sort(key=cmp_to_key(compare))
    return ''.join([str(x) for x in new_list])


a_list = [3,32,321]
a_list.sort(key=cmp_to_key(compare))
print(a_list)
print(''.join([str(x) for x in a_list]))
print(solution(a_list))
