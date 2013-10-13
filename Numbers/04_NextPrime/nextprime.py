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


def main():
    for p in primes():
        print(p)
        if input("Press [Enter] to get new prime, 'q' to quit.") == 'q':
            break


if __name__ == '__main__':
    main()