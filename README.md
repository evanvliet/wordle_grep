wordle_grep
==

A comand line wordle filter, prints possible words.  Use from a bash prompt.

## Synopsis

wordle_grep \<green letters\> \<yellow letters\> \<black letters\> [word list]
 
## Description
Uses sed to print matches to a green, yellow, black specification. The specification is three strings for the green, yellow, and black characters on the wordle puzzle line. Examples:
+ \<green letters\> : *e.g.*, ..a.b  if 3rd and 5th letters are green a and b  
+ \<yellow letters\> : *e.g.*, .e.h if 2nd and 4th letters are yellow e and h  
+ \<black letters\> : *e.g.*, jks if j, k, and s all are black  
Use a dot (.) as a place holder, position significant for green and yellow
letters. 

## Features
+ A plain dot means no characters of a particular color.
+ A previous output list saved in a file can refine a search.

## Dependency
The default word list comes from the pre-New York Times version of wordle.
Uses sed, tr, grep, bash.

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
