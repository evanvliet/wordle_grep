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

A comand line  ilter, prints possible words for the NY Times bee puzzle.  Use from a bash prompt.

## Synopsis

bee_grep abcdefg

## Description

Prints words with initial 'a' character using only letters abcdefg from argument.


