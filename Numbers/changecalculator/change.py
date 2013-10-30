from decimal import Decimal, getcontext

getcontext().prec = 4

denominations = [
    ('dollar', Decimal(1)),
    ('quarter', Decimal(0.25)),
    ('dime', Decimal(0.10)),
    ('nickel', Decimal(0.05)),
    ('penny', Decimal(0.01))
]


def calculate_change(cost, paid):
    change = []
    remaining_change = divmod(paid, cost)[1]
    for n, v in denominations:
        chg = divmod(remaining_change, v)
        if chg[0] > 0:
            change.append((n, chg[0]))
        remaining_change = chg[1]
        if chg[1] == 0:
            break

    return change


def main():
    cost, paid = list(map(Decimal, (input('Enter cost and paid amount: ')).split(' ')))
    if paid < cost:
        print('Paid amount ({0}) is not enough to cover the cost ({1}).'.format(paid, cost))
    elif paid == cost:
        print('Paid amount ({0}) is equal to the cost ({1}). No change will be given.'.format(paid, cost))
    else:
        change = calculate_change(cost, paid)
        print(', '.join(['{0} {1}{2}'.format(tup[1], tup[0], 's' if tup[1] > 1 else '') for tup in change]))


if __name__ == '__main__':
    main()