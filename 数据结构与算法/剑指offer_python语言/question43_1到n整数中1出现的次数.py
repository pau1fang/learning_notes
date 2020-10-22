def sum_of_1(n):
    number = 0
    while n > 0:
        if n % 10 == 1:
            number += 1
        n //= 10
    return number


def solution1(n):
    count = 0
    for i in range(1, n + 1):
        count += sum_of_1(i)
    return count


def solution2(n):
    if n<10:
        return 1
    num_list = list(str(n))
    length = len(num_list)
    if int(num_list[0])>1:
        count = 10**(length-1)
    else:
        count = n-10**(length-1) + 1
    count += int(num_list[0])*(length-1)*10**(length-2)
    num_list.pop(0)
    return count+solution2(int(''.join(num_list)))


print(solution1(123))
print(solution2(123))
