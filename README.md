wordle_guess
==

A comand line wordle guesser, prints suggested word.

## Synopsis

wordle_guess \<green letters\> \<yellow letters\> \<black letters\>
 
## Description
Uses sed to find matches to a green, yellow, black specification. The specification is three strings for the green, yellow, and black characters on the wordle puzzle line. Examples:
+ \<green letters\> : *e.g.*, ..a.b  if 3rd and 5th letters are green a and b  
+ \<yellow letters\> : *e.g.*, .e.h if 2nd and 4th letters are yellow e and h  
+ \<black letters\> : *e.g.*, jks if j, k, and s all are black  
Use a dot (.) as a place holder, position significant for green and yellow
letters.

There is also a python version, at wordle_guess.py.

## Features
+ A plain dot means no characters of a particular color.
+ Picks word that has the most characters in common with other possible matches.
+ With no arguments, scans full word list.  The winner is "arose" - a good first guess.
+ Word list is refined, only last line need be specified.

Consider the following wordle puzzle:

        <wordle_guess.png>

Use wordle guess as follows to get guesses:

    $ ./wordle_search 
    arose 2315
    $ ./wordle_search . ..o.e ars
    lemon 47
    $ ./wordle_search ...o .e..n lm
    enjoy 3
    $ ./wordle_search en.oy . j
    envoy 1

Start without parameters to get arose.
Get second line by engering any green characters - none, yellow o and e with .s to
reflect 3rd and 5th spots, and finally the ars black letters. This yields lemon as the second guess..
Call again with arguments reflectin the colors of any changes from the last line, so ...o for the green o in 4th spot, .e..n for the yellow letters, and lm for the blacks.
Wordle guess suggests enjoy. So calll again wtih updates: en..y for green (no need to enter the o, since it was covered in the last run) and . for no yellow and a j for blacks.
Wordle_guess returns the answer.

Most words solve in 3 or 4 runs. Have no seen it not finding the word.

## Dependency
The default word list comes from the pre-New York Times version of wordle.
Uses sed, tr, grep, bash, uniq.

bee_grep
==

A comand line filter, prints possible words for the NY Times bee puzzle.  Use from a bash prompt.

## Synopsis

bee_grep abcdefg

## Description

Uses sed to filter all words starting with the distinguished letter and having only letters from the puzzle.

gah
==

Guess at hangman, the old unix game, cf. bsdgames. 

## Synopsis

+ get hangman screen in clipboard
+ gah
+ paste clipboard into hangman guess

## Description

Invokes python to match possible words and accumulate counts of words each letter is in,
puts letter that occurs most among possible matches to clipboard as next guess.

## Files
+ gah - hangman guesser
+ gahdict - has word lists by length
+ gah.py - python of course
