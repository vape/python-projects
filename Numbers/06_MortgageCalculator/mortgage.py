def calculate_mortgage(principal_amount, terms, interest):
    i = (interest / 100) / 12
    term_in_months = terms * 12
    return principal_amount * ((i * (1 + i) ** term_in_months) / (((1 + i) ** term_in_months) - 1))


def main():
    inp = input('Enter Principal Amount, Loan Term (years) and annual interest rate as numbers '
                'seperated by space (e.g. 100000 20 5): ')
    amt, terms, interest = map(int, inp.split(' '))
    print('${0:.2f}'.format(calculate_mortgage(amt, terms, interest)))


if __name__ == '__main__':
    main()