import functools
from time import time
from sys import setrecursionlimit
setrecursionlimit(10000)


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]

    return memoizer


@memoize
def fib_recursive(num):
    if num in (0, 1):
        return num
    else:
        return fib_recursive(num - 1) + fib_recursive(num - 2)


def fib_iterative(num):
    if num in (0, 1):
        return num

    x1, x2, xn = 0, 1, 0
    for i in range(2, num + 1):
        xn = x1 + x2
        x1, x2 = x2, xn

    return xn


def main():
    try:
        target = int(input('Enter target number: '))
        fib_func = fib_recursive if 0 <= target <= 1000 else fib_iterative
        start = time()
        res = fib_func(target)
        end = time()
        print('Fib({0}) [{1}]: {2}. Calculated in {3:.3f} seconds.'.format(target, fib_func.__name__, res, (end - start)))
    except ValueError:
        print('Invalid input.')
        exit(1)


if __name__ == '__main__':
    main()