#!/usr/bin/env python3
#
# A comand line wordle player, prints suggested word.
#
# wordle_guess.py <green letters> <yellow letters> <black letters>
#
# Uses python to find matches to a green, yellow, black specification. The
# specification is three strings for the green, yellow, and black
# characters on the last wordle puzzle line. Examples:
#
# <green letters>   e.g., ..a.b if 3rd and 5th letters are green a and b
# <yellow letters>  e.g., .e.h  if 2nd and 4th letters are yellow e and h
# <black letters>   e.g., jks   if j, k, and s all are black
#
# Use a dot (.) as a place holder, as position is significant for green
# and yellow letters. A plain dot means no color character at that spot.
#
# Saves matches to these arguments in a local file for the next guess.
#
# Proceeds to pick a guess from this list. Looks for a word that has
# the most characters in common with other possible matches.  Considers
# most common letters among the matches first. For each character finds
# matches with that letter. If some exist,  use the result for further
# pruning. Prints the final smallest subset.
#
# Called without arguments, it scans a word list from the pre-New York
# Times version of wordle, saved as __file__.replace('.py', '.dat'), e.g.
# wordle_guess.dat. In this case the above algorithm for picking green
# guess suggests "arose" - an ok choice.

import os
import re
import sys
import collections

FULL_LIST = __file__.replace('.py', '.dat')  # From old site
WORD_LIST = "wgp_last"  # Local file holding last matches


def load_words(f):
    return open(f, 'r').readlines() if os.path.isfile(f) else None


# use full list if no words from previous scan or no args
words = load_words(WORD_LIST)
if not words or len(sys.argv) == 1:
    words = load_words(FULL_LIST)

# build regular expression to match green yellow black args
argv = sys.argv[1:]
argv.extend(['.']*3)  # default "." values
(green, yellow, black) = tuple(argv[:3])
# green yellow black patterns to be ORed together and negation taken
# because we can OR patterns in an re but not AND them
# so we test NOT (NOT green or NOT yellow or NOT black)
# to get green AND yellow AND black
gyb = [f"(?!{green})"]  # NOT green
gyb.append(f".*[{black}]")  # NOT black
dots = ''  # to specify position of yellow character
for y in yellow:  # NOT yellow because
    if y != '.':
        gyb.append(f"[^{y}]*$")  # no yellow character
        gyb.append(f"^{dots}{y}")  # has yellow at same spot
    dots = dots + '.'  # add dot to position
gybre = re.compile(f'(?!{"|".join(gyb)})')  # NOT of disjunction

# get possible matches
matches = [word for word in words if gybre.match(word)]
open(WORD_LIST, 'w').write(''.join(matches))  # save for next run
# pick guess from list, first get letters in order most frequent first
letter_counts = collections.Counter(''.join(matches))
letters = [letter for letter, _ in letter_counts.most_common()]
for letter in letters:
    with_letters = [word for word in matches if letter in word]
    if with_letters:  # if letter has matches, use them as new subset
        matches = with_letters
print(matches[0][:-1] if matches else '-no words-')  # suggested guess
