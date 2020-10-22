def add_(num1, num2):
    while num2:
        sum_ = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = sum_
        num2 = carry
    return num1


print(add_(11, 22))
