#!/usr/bin/env python3 
# 
import re
import sys
from collections import Counter

FULL_LIST = "wordle_guess.dat"  # Full word list file
WORD_LIST = "wg_last"  # Local file holding last matches

def load_words(words):
    try:
        file = open(words, 'r')
        return [word.strip() for word in file.readlines()]
    except:
        return []

def mismatch(green, yellow, black):
    gyb = [] 
    # green yellow black patterns to be 'or'ed together and negation taken
    # because we can 'OR' patterns in an re but not 'AND' them
    # so we test NOT (not a or not b or not c or not d or not e)
    # to get a AND b AND c AND d AND e
    gyb.append(f".*[{black}]") # match if any word black character
    gyb.append(f"(?!{green})") # mismatch green characters
    dots='' # to specify position of yellow character
    for y in yellow:
        if y != '.':
            gyb.append(f"[^{y}]*$") # match word without yellow
            gyb.append(f"^{dots}{y}") # match words with yellow at same spot
        dots=dots + '.' # add dot to position
    return re.compile("|".join(gyb))

class WordleGuess:
    def __init__(self, argv):
        self.argv = argv[1:]
        self.argv.extend(['.']*3)
        self.words = load_words(WORD_LIST)
        if not self.words or 1 == len(argv):
            self.words = load_words(FULL_LIST)
            
    def match(self):
        gyb_mis = mismatch(self.argv[0], self.argv[1], self.argv[2])
        matches = [word for word in self.words if not gyb_mis.match(word)]
        self.words = matches

    def save(self):
        with open(WORD_LIST, 'w') as file:
            file.write('\n'.join(self.words))

    def guess(self):
        letter_counts = Counter(''.join(self.words))
        letters = [letter for letter, _ in letter_counts.most_common()]
        for letter in letters:
            subset = [word for word in self.words if letter in word]
            if subset:
                self.words = subset
        return self.words[0] if self.words else ''

if __name__ == "__main__":
    # wg = WordleGuess("prog . ...s aroe".split()) #sys.argv)
    wg = WordleGuess(sys.argv)
    wg.match()
    wg.save()
    print(wg.guess())
