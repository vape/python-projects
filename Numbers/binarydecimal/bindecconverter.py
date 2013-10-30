def main():
    num, target_base = input('Enter number and what base to convert to (e.g. 1001110101 d [binary to decimal] or '
                             '3442383942 b [decimal to binary]): ').split(' ')
    if target_base not in ('d', 'b'):
        print('Unrecognized base')
        exit(1)

    print(int(num, 2) if target_base == 'd' else bin(int(num))[2:])

if __name__ == '__main__':
    main()