from math import sqrt


def primes():
    current = 2
    while True:
        if is_prime(current):
            yield current
        current += 1


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


def factor_primes(num):
    if is_prime(num):
        return [num]

    current_num = num
    factors = []
    while current_num > 1:
        for p in primes():
            res = divmod(current_num, p)
            if res[1] == 0:
                factors.append(p)
                current_num = res[0]
                break

    return factors


def main():
    print(factor_primes(int(input('Enter number: '))))


if __name__ == '__main__':
    main()