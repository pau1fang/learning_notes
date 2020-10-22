from functools import wraps
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    i = 2
    fib_one = 0
    fib_two = 1
    fib_n = 0
    while i <= n:
        fib_n = fib_one + fib_two
        fib_one = fib_two
        fib_two = fib_n
    return fib_n


print(fib(5))

def cache(func):
    mid = {}
    @wraps(func)
    def wrapper(n):
        res = mid.get(n)
        if res:
            return res
        else:
            res = func(n)
            mid[n] = res
            return res
    return wrapper


@cache
def fib3(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib3(5))
