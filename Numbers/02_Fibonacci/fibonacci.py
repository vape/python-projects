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


def main():
    try:
        target = min(10000, int(input('Enter target number [0, 1500]: ')))
        start = time()
        res = fib_recursive(target, target)
        end = time()
        print('Fib({0}) [Recursive]: {1}. Calculated in {2:.3f} seconds.'.format(target, res, (end - start)))
    except ValueError:
        print('Invalid input.')
        exit(1)


if __name__ == '__main__':
    main()