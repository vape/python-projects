from sys import argv
from itertools import takewhile

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")


def pig_latinize(word):
    if word[0] in consonants:
        cons = list(takewhile(lambda l: l in consonants, word))
        return '{0}{1}ay'.format(word[len(cons):], ''.join(cons))
    else:
        return word + 'way'


def main(argv):
    txt = ' '.join(argv[1:]) if len(argv) > 1 else input('Please enter text to pig-latinize: ')
    print(' '.join(map(pig_latinize, [t.lower() for t in txt.split(' ') if t])))


if __name__ == '__main__':
    main(argv)