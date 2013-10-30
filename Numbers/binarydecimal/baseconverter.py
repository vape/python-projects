
# 0-9A-Z characters used in conversion. Up to base 36 is supported.
chars = [chr(i) for i in list(range(48, 58)) + list(range(65, 91))]


def convert_to_decimal(num, src_base):
    dec_num = 0
    rev_num = num[::-1]
    for i in range(0, len(num)):
        dec_num += chars.index(rev_num[i]) * (int(src_base)**i)

    return dec_num


def convert_decimal_to_base(num, target_base):
    digits = []
    target_base = int(target_base)
    remainder = num
    while True:
        rem = divmod(remainder, target_base)
        digits.insert(0, rem[1])
        remainder = rem[0]

        if rem[0] < target_base:
            digits.insert(0, rem[0])
            break

    return ''.join(map(str, digits))


def guess_number_base(num):
    try:
        return max([chars.index(n) for n in num]) + 1
    except ValueError:
        return -1


def main():
    inputs = input('Enter number, (optionally) base of number, and base to convert to'
                   '(e.g. 1234 10 2 [decimal to binary] or 1234 2 [base 5 to binary]): ').split(' ')
    if len(inputs) not in (2, 3):
        print('You must enter 2 or 3 numbers as inputs.')
        exit()

    if len(inputs) == 2:
        num, target_base = inputs
        src_base = guess_number_base(num)
        if src_base == -1:
            print('Unsupported number. You can enter numbers up to base 36.')
            exit()
        print('Number will be processed as base {0}.'.format(src_base))
    else:
        num, src_base, target_base = inputs

    dec = convert_to_decimal(num, src_base)
    res = convert_decimal_to_base(dec, target_base)
    print('{0} (base {1}) in base {2} is {3}.'.format(num, src_base, target_base, res))


if __name__ == '__main__':
    main()