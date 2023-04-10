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


def ghs():
    """
    get last lines of clipboard containing hangman screen
    """
    s = check_output('pbpaste').decode('utf-8').split('\n')
    for k in range(len(s)-1, 0, -1):
        if s[k][:5] == 'Guess':
            return s[k-9:k]


class Hangman:  # guess for hangman

    def __init__(self):
        try:
            s = ghs()
            self.guess = set(s[0].split()[-1])
            self.word = s[-1].split()[-1]
            self.length = len(self.word)
            self.wrong = self.guess - set(self.word)
            self.counter = Counter()
            self.answers = []
            self.map = str.maketrans(ascii_lowercase, "".join([l
                if l in self.word else "-" for l in ascii_lowercase]))
        except:
            print("bad screen")
            quit()

    def suggest(self):
        '''get best guess'''
        return self.counter.most_common(1)[0][0].encode('utf-8')

    def guesses(self, nguess):
        '''string containing nguest best guesses with counts'''
        return '\n'.join(f"{c[0]} {c[1]}"
            for c in hangman.counter.most_common(nguess))

    def check(self, word):
        '''Check length, no bad guessed, matches guessed.'''
        right = set(word)
        if not right & self.wrong and word.translate(self.map) == self.word:
            self.counter.update([c for c in right - self.guess])
            self.answers.append(word)
            return True
        return False


if __name__ == '__main__':
    hangman = Hangman()
    for line in open("hg.dat"):
        word = line.strip()
        if len(word) < hangman.length:
            continue
        if len(word) > hangman.length:
            break
        hangman.check(word)

    # print first 8 answers, number of possible words and best three guesses
    print('\n'.join(hangman.answers[:8]))
    print(f"--- {len(hangman.answers)} ---")
    print(hangman.guesses(3))

    # paste best guess
    Popen('pbcopy', stdin=PIPE).communicate(hangman.suggest())