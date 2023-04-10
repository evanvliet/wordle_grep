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
    for k in range(len(s)-1, 0, -1):
        if 'Guess' in s[k]:
            return s[k-9:k]
 
class Hangman:  # guess for hangman

    def __init__(self):
        try:
            s = ghs()
            self.guess = set(re.search(r'Guessed: +([a-z]*)', s[0]).group(1))
            self.word = re.search(r'Word: +([-a-z]*)', s[-1]).group(1)
            self.length = len(self.word)
            self.wrong = self.guess - set(self.word)
            self.counter = collections.Counter()
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
        right = set(word)
        if not right & self.wrong and word.translate(self.map) == self.word:
            self.counter.update([c for c in right - self.guess])
            return True
        return False

if __name__ == '__main__':
    hangman = Hangman()
    nm = 0
    for line in open("hg.dat"):
        word = line.strip()
        if len(word) < hangman.length:
            continue
        if len(word) > hangman.length:
            break
        if hangman.check(word):
            nm += 1
            if nm <= 8:
                print(line, end='')
    if nm >8:
        print(f"--- {nm} ---")
    print(hangman.suggest())
