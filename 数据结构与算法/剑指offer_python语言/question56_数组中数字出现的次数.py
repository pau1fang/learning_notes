def find_numbers_appear_once(arr):
    result_exclusive_or = 0
    for i in arr:
        result_exclusive_or ^= i
    number1 = 0
    number2 = 0
    index_bit = find_first_bit_is_1(result_exclusive_or)
    for i in arr:
        if is_bit_1(i, index_bit):
            number1 ^= i
        else:
            number2 ^= i
    return number1, number2


def find_first_bit_is_1(num):
    index_bit = 0
    while (num&1)==0 and index_bit < 8*4:
        num >> 1
        index_bit += 1
    return index_bit


def is_bit_1(num, index_bit):
    num >> index_bit
    return num & 1


array = [1,2,3,4,5,6,5,4,3,2]
print(find_numbers_appear_once(array))


"""
题目二：数组中唯一只出现一次的数字
"""


def find_number_appear_once(arr):
    bit_sum = [0 for _ in range(32)]
    for i in arr:
        index = 31
        while i and index >=0:
            bit_sum[index] += i & 1
            index -= 1
            i >>= 1

    number = 0
    for i in bit_sum:
        number <<= 1
        number += i % 3
    return number


find = find_number_appear_once([10,10,10,1])

print(find)
