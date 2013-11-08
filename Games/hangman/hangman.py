from os import path, remove
from requests import get
from bs4 import BeautifulSoup
import re
from random import choice
from string import ascii_uppercase

max_guesses = 9


def construct_word_db():
    words = []
    rgx = re.compile('^[a-zA-Z]+$')
    try:
        for i in range(1, 16):
            soup = BeautifulSoup(get('http://www.manythings.org/vocabulary/lists/l/words.php?f=noll{0:02d}'.format(i),
                                     headers={
                                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}).text)
            [words.append(t.text) for t in soup.select('div.co ul li')]

        with open('words.txt', 'w') as file:
            [file.write(w.lower() + '\n') for w in list(set(words)) if len(w) > 5 and re.match(rgx, w)]
    except:
        print('Gah! Something went wrong. Please try again. Thanks!')


def get_word():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        return choice(words) if words else ''


def report_game_progress(num_guesses, guessed_word):
    print('{0} || {1} guesses. ({2} guesses left).'.format(' '.join(guessed_word), num_guesses, max_guesses - num_guesses))


def find_all_indexes(letter, word):
    return [i for i, l in enumerate(word) if l == letter]


def replace_on_indexes(letter, word, indexes):
    new_word = []
    for i, l in enumerate(word):
        new_word.append(letter if i in indexes else l)
    return ''.join(new_word)

def play_hangman(word):
    word = word
    num_guesses = 0
    guessed_word = '_' * len(word)
    previous_guesses = []
    while num_guesses < max_guesses and guessed_word != word:
        report_game_progress(num_guesses, guessed_word, word)
        inp = input('Guess letter or the whole word: ').upper()
        if len(inp) > 1:
            if inp == word:
                guessed_word = word
                break
            else:
                print('Sorry. The word is not {0}.'.format(inp))
                continue
        if inp not in ascii_uppercase:
            print('Your guess should be an English uppercase letter.')
            continue
        if inp in previous_guesses:
            print('You\'ve guessed this letter before. Pay attention :)')
            continue

        print('You\'ve guessed {0}'.format(inp))
        previous_guesses.append(inp)
        num_guesses += 1
        if inp not in word:
            print('Sorry! The word has no {0}s in it.'.format(inp))
        else:
            indexes = find_all_indexes(inp, word)
            guessed_word = replace_on_indexes(inp, guessed_word, indexes)
            print('Yay! The word has {0} {1}s in it.'.format(len(indexes), inp))

    print('')
    if word == guessed_word:
        print('Yay! You\'ve guessed the word correctly in {0} attempts.'.format(num_guesses))
    else:
        print('Sorry! You\'ve lost the game. The word was "{0}".'.format(word))


def main():
    if not path.exists('words.txt'):
        print('One moment. Constructing word database for hangman...')
        construct_word_db()

    while True:
        word = get_word()
        if not word:
            remove('words.txt')
            print('Oops! Something went wrong. Please run the game again.')
            break

        play_hangman(word.upper())
        inp = input('Press Q to quit, [Enter] to play another game: ')
        if inp.lower() == 'q':
            print('Bye!')
            break


if __name__ == '__main__':
    main()