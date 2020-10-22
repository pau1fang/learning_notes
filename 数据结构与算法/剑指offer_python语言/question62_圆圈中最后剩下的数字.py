def solution(n, m):
    arr = list(range(n))
    index = m-1
    while len(arr) >1:
        index %= len(arr)
        arr.pop(index)
        index += m-1
    print(arr)


def solution2(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n+1):
        last = (last + m) % i
    return last


solution(5, 3)
print(solution2(5, 3))
