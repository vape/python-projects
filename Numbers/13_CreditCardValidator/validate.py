import sys


def main(argv):
    if len(argv) < 2:
        return print('Please specify credit card number to validate.')

    num = list(map(int, list(argv[1])))
    checkvals = []
    checkdigits = list(range(len(num)-2, -1, -2))
    for i, digit in enumerate(num):
        if i in checkdigits:
            digit = digit*2 if digit < 5 else sum(map(int, list(str(digit*2))))
        checkvals.append(digit)

    print('The number {0} is {1}.'.format(argv[1], 'valid' if sum(checkvals)%10 == 0 else 'invalid'))


if __name__ == '__main__':
    main(sys.argv)