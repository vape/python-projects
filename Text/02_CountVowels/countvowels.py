from sys import argv
from itertools import groupby

vowels = list("aeiou")


def main(argv):
    txt = ' '.join(argv[1:]) if len(argv) > 1 else input('Please enter text to count vowels: ')
    vows = [v for v in txt.lower() if v in vowels]
    groups = {}
    print('{0} vowels in text.'.format(len(vows)))
    for k, g in groupby(sorted(vows)):
        groups[k] = len(list(g))

    print('Vowel stats: {0}'.format(', '.join(['{0}: {1}'.format(k, groups[k]) for k in groups.keys()])))


if __name__ == '__main__':
    main(argv)
