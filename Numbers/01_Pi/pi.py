from math import sqrt
from decimal import Decimal, getcontext
getcontext().prec = 50

def gauss_legendre():
    a = [Decimal(1)]
    b = [Decimal(1)/Decimal(sqrt(2))]
    t = [Decimal(0.25)]
    p = [Decimal(1)]

    for i in range(0, 20):
        n = i
        a.append(Decimal((a[n] + b[n])) / Decimal(2))
        b.append(Decimal(sqrt(a[n] * b[n])))
        t.append(t[n] - (p[n] * ((a[n] - a[n+1])**2)))
        p.append(p[n] * 2)

        pi = ((a[n+1] + b[n+1])**2) / (4 * t[n+1])
        print(format(pi, '.50f'))


def main():
    gauss_legendre()
    pass


if __name__ == "__main__":
    main()