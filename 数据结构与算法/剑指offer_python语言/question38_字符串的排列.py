from itertools import permutations, combinations

s = "abc"
print(list(permutations(s)))

result = []
count = 1


def per(arr, start, end):
    global count
    if start < end:
        # per(arr, start+1, end)
        for i in range(start, end+1):
            arr[start], arr[i] = arr[i], arr[start]
            # result.append(arr[:])
            per(arr, start + 1, end)
            arr[start], arr[i] = arr[i], arr[start]
    else:
        print(f'第{count}个排列为：{" ".join(arr)}')
        count += 1


def comb(arr, n):
    if n>=0:
        if n == 0:
            yield ''
            return
        if len(arr) == n:
            yield ''.join(arr)
        else:
            res = arr[0]
            for i in comb(arr[1:], n-1):
                yield res+i
            for i in comb(arr[1:], n):
                yield i


def comb2(arr, start, length, m):
    if length - start >= m:
        if length-start == m:
            yield ''.join([arr[i] for i in range(start, length)])
        else:
            first = arr[start]
            if m == 1:
                yield first
            else:
                for rest in comb2(arr, start+1, length, m-1):
                    yield first+rest
            for i in comb2(arr, start+1, length, m):
                yield i


def comb3(arr, start, length, m, str_arr):
    if m == 0:
        for i in str_arr:
            print(i, end=' ')
        print()
        return
    if start >= length:
        return
    str_arr.append(arr[start])
    comb3(arr, start+1, length, m-1, str_arr)
    str_arr.pop()
    comb3(arr, start+1, length, m, str_arr)


def combination(arr):
    for i in range(1, len(arr)+1):
        for j in comb(arr, i):
            print(j)


print(result)
s = list("abc")
per(s, 0, len(s)-1)
# for x in comb(list('abc'), 3):
#     print(x)

# combination(s)
# for x in comb2(s, 0, len(s), 3):
#     print(x)
str_arr_ = []
# comb3(s, 0, len(s), 1, str_arr_)
for x in range(1, len(s)+1):
    comb3(s, 0, len(s), x, str_arr_)
