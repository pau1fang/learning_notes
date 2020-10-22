def print_number(number):
    begin = False
    for s in number:
        if not begin and s != '0':
            begin = True
        if begin:
            print(s, end='')
    if begin:
        print(end='\t')


def print1_to_max_of_n(number, length, index):
    if index == length - 1:
        print_number(number)
        return
    for i in range(10):
        number[index + 1] = chr(i + ord('0'))
        print1_to_max_of_n(number, length, index+1)


def print_1_to_max(n):
    if n<1:
        return
    number = ['0' for _ in range(n)]
    for i in range(10):
        number[0] = chr(i + ord('0'))
        print1_to_max_of_n(number, n, 0)


def increment(number):
    is_overflow = False
    n_take_over = 0
    for i in range(len(number)-1, -1, -1):
        n_sum = ord(number[i]) - ord('0') + n_take_over
        if i == len(number) - 1:
            n_sum += 1
        if n_sum >= 10:
            if i == 0:
                is_overflow = True
            else:
                n_sum -= 10
                n_take_over = 1
                number[i] = chr(ord('0')+n_sum)
        else:
            number[i] = chr(ord('0')+n_sum)
            break
    return is_overflow


def solution2(n):
    if n<=0:
        return
    number = ['0' for _ in range(n)]
    while increment(number) is not True:
        print_number(number)


# print_number('3248432943')
print_1_to_max(2)
print()
solution2(2)
