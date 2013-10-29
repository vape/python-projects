from sys import argv
from math import floor


def is_palindrome3(txt):
    """
    Checks if the txt is a palindrome by reversing the text
    and checking if it's equal to the original text.
    :param txt:
    :return:
    """
    return False if not txt or len(txt) == 1 else txt == txt[::-1]


def is_palindrome2(txt):
    """
    Checks if the txt is a palindrome by splitting the text in half
    and checking for equality.
    :param txt:
    :return:
    """
    return False if not txt or len(txt) == 1 else txt[0:floor(len(txt)/2)] == txt[-1:-1*floor(len(txt)/2)-1:-1]


def is_palindrome(txt):
    """
    Checks if the txt is a palindrome by iterating over the text
    letter by letter from the beginning and the end and checking
    for equality.
    :param txt:
    :return:
    """
    if not txt:
        return False

    for i, c in enumerate(txt[0:floor(len(txt)/2)]):
        if txt[i] != txt[-1*(i+1)]:
            return False
    return True


def main(argv):
    txt = ' '.join(argv[1:]) if len(argv) > 1 else input('Please enter text to check for palindrome: ')
    print('The text is{0}a palindrome.'.format(' ' if is_palindrome3(txt.lower()) else ' not '))


if __name__ == '__main__':
    main(argv)