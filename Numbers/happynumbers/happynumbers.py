def is_happy(num):
    seq = []
    while num != 1:
        num = sum(map(lambda x: x**2, map(int, str(num))))
        if num in seq:
            return False
        seq.append(num)
    return True


def happy_numbers():
    """
    Generator which returns happy numbers.
    """
    num = 0
    while True:
        num += 1
        if is_happy(num):
            yield num


def main():
    for i in happy_numbers():
        print(i)


if __name__ == '__main__':
    main()