def solution(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    product = [0 for _ in range(length + 1)]
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3
    for i in range(4, length + 1):
        max_ = 0
        for j in range(1, i // 2 + 1):
            if max_ < product[j] * product[i - j]:
                max_ = product[j] * product[i - j]
            product[i] = max_
    max_ = product[length]
    print(product)
    return max_


def solution2(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    times_of_3 = length // 3
    if length - times_of_3*3 == 1:
        times_of_3 -= 1
    times_of_2 = (length - times_of_3*3)//2
    return pow(3, times_of_3) * pow(2, times_of_2)


if __name__ == '__main__':
    print(solution(10))
    print(solution2(10))
