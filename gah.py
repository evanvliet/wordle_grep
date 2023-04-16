#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" gah.py file

    clipboard contains screen of playing hangman.
    extract Guessed: string
    extract Word: string
    construct suggested letter and paste to clipboard
    print possible words
    search for matches to word excluding guessed letters
"""

from string import ascii_lowercase
from collections import Counter
from subprocess import check_output, Popen, PIPE


def copy_char(c):
    """ copy character to clipboard """
    Popen('pbcopy', stdin=PIPE).communicate(c)


def get_screen():
    """ get guessed and word from clipboard containing hangman screen """
    def last_word(s): return s.split()[-1]
    s = check_output('pbpaste').decode('utf-8').split('\n')
    for k in range(len(s)-1, 0, -1):
        if s[k][1:6] == 'Word:':
            return (last_word(s[k-8]), last_word(s[k]))


class Gah:  # guess at hangman

    def __init__(self, guess, word):
        self.word = word
        self.guess = set(guess)
        self.wrong = self.guess - set(self.word)
        self.data = f'gahdict/{len(self.word)}'
        self.counter = Counter()
        self.map = str.maketrans(ascii_lowercase, "".join(
            [l if l in self.word else "-" for l in ascii_lowercase]))

    def suggest(self):
        '''letter that occurs in most possible words'''
        return self.counter.most_common(1)[0][0].encode('utf-8')

    def check(self, word):
        '''Check for wrong letters guessed and matches right ones.'''
        if set(word) & self.wrong or word.translate(self.map) != self.word:
            return False
        # increment count for each word occurrence (vs character)
        self.counter.update([c for c in set(word) - self.guess])
        return True


if __name__ == '__main__':
    gah = Gah(*get_screen())
    for line in open(gah.data):
        if gah.check(line.strip()):
            print(line, end='')
    # copy suggestion to clipboard
    copy_char(gah.suggest())
