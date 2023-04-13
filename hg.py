#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" hg.py file

    clipboard contains screen of playing hangman.
    extract Guessed: string
    extract Word: string
    construct suggested letter
    search for matches to word excluding guessed letters
"""

from string import ascii_lowercase
from collections import Counter
from subprocess import check_output, Popen, PIPE


def copy_char(c):
    """
    copy character to clipboard
    """
    Popen('pbcopy', stdin=PIPE).communicate(c)


def get_screen():
    """
    get guessed and word from clipboard containing hangman screen
    """
    def last_word(s): return s.split()[-1]
    s = check_output('pbpaste').decode('utf-8').split('\n')
    for k in range(len(s)-1, 0, -1):
        if s[k][:5] == 'Guess':
            return (last_word(s[k-9]), last_word(s[k-1]))


class Hangman:  # guess for hangman

    def __init__(self, guess, word):
        self.word = word
        self.guess = set(guess)
        self.wrong = self.guess - set(self.word)
        self.data = f'hgdat/{len(self.word)}'
        self.counter = Counter()
        self.map = str.maketrans(ascii_lowercase, "".join(
            [l if l in self.word else "-" for l in ascii_lowercase]))

    def suggest(self):
        '''get best guess'''
        return self.counter.most_common(1)[0][0].encode('utf-8')

    def check(self, word):
        '''Check for wrong letters guessed and matches right ones.'''
        if set(word) & self.wrong:
            return False
        if word.translate(self.map) == self.word:
            self.counter.update([c for c in set(word) - self.guess])
            return True
        return False


if __name__ == '__main__':
    try:
        hangman = Hangman(*get_screen())
        for line in open(hangman.data):
            word = line.strip()
            if hangman.check(word):
                print(word)
        # copy suggestion to clipboard
        copy_char(hangman.suggest())

    except:
        print('bad screen')
        quit()
