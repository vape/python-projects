from random import randrange


def josephus(n, k):
    if n == 1:
        return 1
    else:
        return ((josephus(n - 1, k) + k - 1) % n) + 1


def main():
    count = randrange(10, 100)
    print(count, josephus(count, 3))


if __name__ == '__main__':
    main()