#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" hg.py file

    clipboard contains screen of playing hangman.
    extract Guessed: string
    extract Word: string
    construct suggested letter
    search for matches to word excluding guessed letters
"""

import re
import string
import collections
from subprocess import call, check_output, Popen, PIPE


def ghs():
    """
    get last lines of clipboard containing hangman screen
    """
    s = check_output('pbpaste').decode('utf-8').split('\n')
    k = len(s)
    while k:
        k = k - 1
        if 'Guess' in s[k]:
            return '\n'.join(s[k-12:k])
    return ''
 
class Hangman:  # guess for hangman

    def __init__(self):
        try:
            screen = ghs()
            self.counter = collections.Counter()
            self.guess = set(re.search(r'Guessed: +([a-z]*)', screen).group(1))
            self.word = re.search(r'Word: +([-a-z]*)', screen).group(1)
            self.length = len(self.word)
            self.exclusions = self.guess - set(self.word)
            self.map = str.maketrans(string.ascii_lowercase, "".join([l
                if l in self.word else "-" for l in string.ascii_lowercase]))
        except:
            print("bad screen")
            quit()

    def suggest(self):
        next_letter = self.counter.most_common(1)[0][0]
        process = Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=PIPE)
        process.communicate(next_letter.encode('utf-8'))
        return '\n'.join(f"{c[0]} {c[1]}"
                for c in self.counter.most_common(3))

    def check(self, word):
        '''Check length, no bad guessed, matches guessed.'''
        return (len(word) == self.length
            and not set(word) & self.exclusions
            and word.translate(self.map) == self.word
            or self.counter.update([c for c in set(word) - self.guess]))

if __name__ == '__main__':
    hangman = Hangman()
    nm = 0
    for line in open("hg.dat"):
        if hangman.check(line.strip()):
            nm += 1
            if nm <= 8:
                print(line, end='')
    if nm >8:
        print(f"--- {nm} ---")
    print(hangman.suggest())
