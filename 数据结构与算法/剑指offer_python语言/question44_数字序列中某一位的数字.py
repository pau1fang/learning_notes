def solution(index):
    if index < 0:
        return -1
    digits = 1
    while True:
        if digits == 1:
            numbers = 10
        else:
            numbers = 9*pow(10, (digits-1))
        if index < digits * numbers:
            return digit_at_index2(index, digits)
        index -= numbers*digits
        digits += 1


def digit_at_index(index, digits):
    n = index//digits
    digit = index%digits
    num = n+begin_number(digits)
    return str(num)[digit]


def digit_at_index2(index, digits):
    n = digits - index%digits
    num = index//digits + begin_number(digits)
    while n > 1:
        num //= 10
        n -= 1
    return num%10


def begin_number(digits):
    if digits==1:
        return 0
    return pow(10, digits-1)


print(solution(1001))
