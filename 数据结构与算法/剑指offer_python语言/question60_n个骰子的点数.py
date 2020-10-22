def solution1(n):
    count = [0 for _ in range(5 * n + 1)]
    s = 0
    helper(n, n, count, s)
    sum_ = pow(6, n)
    result = [x / sum_ for x in count]
    for x, y in zip(count, result):
        print("{}:  {}".format(x, y))


def helper(n, k, count, s):
    if k == 1:
        for i in range(1, 7):
            count[s - n + i] += 1
    else:
        for i in range(1, 7):
            helper(n, k - 1, count, s + i)


def solution2(n):
    if n < 1:
        return
    a = [0 for _ in range(6 * n + 1)]
    b = [0 for _ in range(6 * n + 1)]
    for i in range(1, 7):
        a[i] = 1
    k = n
    while k > 0:
        for i in range(n, 6 * n + 1):
            b[i] = a[i - 6] + a[i - 5] + a[i - 4] + a[i - 3] + a[i - 2] + a[i - 1]
        a, b = b, a
        k -= 1

    print(b)


def print_probability(number):
    if number < 1:
        return
    probabilities = [[0 for _ in range(6 * number + 1)] for _ in range(2)]
    flag = 0
    for i in range(1, 7):
        probabilities[0][i] = 1
    for k in range(2, number + 1):
        for i in range(k):
            probabilities[1 - flag][i] = 0
        for i in range(k, 6 * k + 1):
            probabilities[1 - flag][i] = 0
            j = 1
            while j <= i and j <= 6:
                probabilities[1 - flag][i] += probabilities[flag][i - j]
                j += 1
        flag = 1 - flag
    print(probabilities[flag])


solution1(2)
solution2(3)
print_probability(3)
