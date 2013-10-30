from Numbers.common.prime import is_prime, primes


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