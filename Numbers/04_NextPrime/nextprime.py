from Numbers.common.prime import primes


def main():
    for p in primes():
        print(p)
        if input("Press [Enter] to get new prime, 'q' to quit.") == 'q':
            break


if __name__ == '__main__':
    main()