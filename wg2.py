
#!/usr/bin/env python3 
import os 
import sys 
# A command line wordle player, prints suggested word. 
# wordle_guess 
# Uses sed to find matches to a green, yellow, black specification. The 
# specification is three strings for the green, yellow, and black 
# characters on the last wordle puzzle line. Examples: 
# 
# e.g., ..a.b if 3rd and 5th letters are green a and b 
# e.g., .e.h if 2nd and 4th letters are yellow e and h 
# e.g., jks if j, k, and s all are black 
# 
# Use a dot (.) as a place holder, as position is significant for green 
# and yellow letters. A plain dot means no color character at that spot. 
# 
# Saves the sed output of matching words in local file for next guess. 
# 
# Proceeds to pick a guess from this output. Looks for a word that has 
# the most characters in common with other possible matches. Considers 
# most common letters among the matches first. For each character finds 
# matches with that letter. If some exist, use the result for further 
# pruning. Prints the final smallest subset. 
# 
# Called without arguments, it scans a word list from the pre-New York 
# Times version of wordle, saved as $BASH_SOURCE.dat, e.g. 
# wordle_guess.dat. In this case the above algorithm for picking a 
# guess suggests "arose" - an ok choice. 
FULL_LIST = os.path.basename(sys.argv[0]) + ".dat" # full list from old wordle site 
WORD_LIST = "wg_last" # local file holding last matches 
MATCHES = "/var/tmp/wg_match" # work copy of current scan 
# get sed commands for wordle matching 
def sed_commands(): 
 return [ 
 "^{}/!d".format(sys.argv[1] if len(sys.argv) > 1 else "."), 
 "[{0}]/{0}/d".format(sys.argv[3] if len(sys.argv) > 3 else "."), 
 ] + ["^{}{}/d".format("."*(x-1), y) for x, y in enumerate(sys.argv[2] if len(sys.argv) > 2 else ".", start=1)] 
# get possible matches 
def get_matches(): 
 if len(sys.argv) > 1: 
 os.system("sed -e '{}' {} > {}".format(";".join(sed_commands()), FULL_LIST, MATCHES)) 
 else: 
 os.system("cp {} {}".format(FULL_LIST, WORD_LIST)) 
# pick guess from list. first get letters in order most frequent first 
def pick_guess(): 
 letters = [x for x in open(MATCHES).read() if x.isalpha()] 
 with_letter = open("/var/tmp/wg_with_letter", "w") 
 for letter in sorted(set(letters), key=lambda x: letters.count(x), reverse=True): 
 new_matches = [m for m in open(MATCHES).read().split() if letter in m] 
 with_letter.write("\n".join(new_matches) + "\n") 
 with_letter.close() 
 os.rename("/var/tmp/wg_with_letter", MATCHES) 
 return open(MATCHES).readline().strip() 
# clean up 
def clean_up(): 
 os.remove(MATCHES) 
if 
name
 == "
main
": 
 get_matches() 
 print(pick_guess()) 
 clean_up() ```