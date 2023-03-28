#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" hg.py file

    clipboard contains screen of playing hangman.
    extract g Guessed: string
    extract w Word: string
    construct s Answer: string
    search dictionary for matches to s excluding g - w (exclusions)

"""

import re
import string
import collections
from subprocess import call, check_output, Popen, PIPE
import sys

class Hangman:  # guess for hangman

    def __init__(self, fn):
        screen = check_output('pbpaste').decode('utf-8')
        try:
            reguess = r'Guessed: +([a-z]*)'
            reword = r'Word: +([-a-z]*)'
            self.guess = set(re.search(reguess, screen).group(1))
            self.word = re.search(reword, screen).group(1)
            self.length = len(self.word)
            letters = set(self.word)
            self.exclusions = self.guess - letters
            intab = string.ascii_lowercase
            outtab = "".join([l if l in letters else "-" for l in intab])
            self.map = str.maketrans(intab, outtab)
            self.counter = collections.Counter()
        except:
            print("bad screen")
            quit()

    def cch(self, word):
        '''Maintain count of words per unguessed character.'''
        self.counter.update([c for c in set(word) - self.guess])
        return True

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
            and self.cch(word))

if __name__ == '__main__':
    hangman = Hangman("hg")
    nm = 0
    for line in open(sys.argv[1]):
        if hangman.check(line.strip()):
            nm += 1
            if nm <= 8:
                print(line, end='')
    if nm >8:
        print(f"--- {nm} ---")
    print(hangman.suggest())
