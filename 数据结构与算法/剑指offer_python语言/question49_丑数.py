def solution1(n):
    ugly_count = 0
    number = 0
    while ugly_count<n:
        number += 1
        if is_ugly(number):
            ugly_count += 1
    return number


def is_ugly(number):
    while number%2 == 0:
        number //= 2
    while number%3 == 0:
        number//= 3
    while number%5 == 0:
        number //= 5
    return number==1


def solution2(index):
    if index <= 0:
        return 0

    ugly_numbers = [0 for _ in range(index)]
    ugly_numbers[0] = 1
    index_2 = 0
    index_3 = 0
    index_5 = 0
    next_ugly_index = 1

    while next_ugly_index < index:
        next_ugly_number = min(ugly_numbers[index_2] * 2,
                               ugly_numbers[index_3] * 3,
                               ugly_numbers[index_5] * 5
                               )
        ugly_numbers[next_ugly_index] = next_ugly_number
        while ugly_numbers[index_2] * 2 <= next_ugly_number:
            index_2 += 1
        while ugly_numbers[index_3] * 3 <= next_ugly_number:
            index_3 += 1
        while ugly_numbers[index_5] * 5 <= next_ugly_number:
            index_5 += 1
        next_ugly_index += 1
        print(next_ugly_number)
    return ugly_numbers[index-1]


# print(solution2(1500))
solution2(20)
