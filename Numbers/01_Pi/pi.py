from time import time


def pi_spigot():
    """
    Generator function based on Jeremy Gibbons's spigot algorithm
    [http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf]
    Yields digits of pi indefinitely.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


def calculate_pi(num_digits):
    start = time()
    digits = []
    current_digit = 0
    for d in pi_spigot():
        current_digit += 1
        digits.append(str(d))
        if current_digit > num_digits:
            break

    end = time()
    return ''.join(digits[1:]), (end - start)


def print_in_blocks(lst, size):
    num_blocks = int(len(lst) / size) + 1
    for i in range(0, num_blocks):
        print(''.join(lst[i*size:(i*size)+size]))


def main():
    try:
        num_digits = min(30000, int(input("Please enter the number of digits [1, 30000]: ")))
        print('Calculating {0} digits of PI'.format(num_digits))
    except Exception as e:
        print(e)
        exit(1)

    pi_digits, elapsed = calculate_pi(num_digits)
    print('Here is {0} digits of PI calculated in {1:.3f} seconds.'.format(num_digits, elapsed))
    print('3.')
    print_in_blocks(pi_digits, 40)


if __name__ == "__main__":
    main()