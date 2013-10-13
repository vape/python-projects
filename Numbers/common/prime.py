from math import sqrt


def is_prime(num):
    if num in (0, 1):
        return False
    if num in (2, 3):
        return True
    if int(str(num)[-1]) % 2 == 0:
        return False
    if sum(map(int, str(num))) % 3 == 0 or sum(map(int, str(num))) % 9 == 0:
        return False
    if len(str(num)) >= 2 and int(str(num)[-2:]) % 4 == 0:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primes():
    """
    A generator which yields primes using a naive algorithm.
    Increments numbers and checks if the number is prime
    using the is_prime method.
    """
    current = 2
    while True:
        if is_prime(current):
            yield current
        current += 1


def generate_primes(max_num):
    """
    Generates a list of primes using the
    `Sieve of Eratosthenes <http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`_ method.
    :param max_num: Max value to use in the sieve
    :return: list of primes up to max_num
    """
    rng = list(range(2, max_num+1))
    if max_num <= 3:
        return list(range(2, max_num+1))

    p = 2
    while p <= max_num:
        p_increments = list(range(p, max_num, p))
        if len(p_increments) <= 1:
            break
        for i in p_increments:
            if rng[i-2] != p:
                rng[i-2] = 0
        p += 1

    return [v for v in rng if v != 0]