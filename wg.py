import re
import sys
from collections import Counter

FULL_LIST = "wordle_guess.dat"  # Full word list file
WORD_LIST = "wg_last"  # Local file holding last matches

def load_word_list(word_list):
    try:
        file = open(word_list, 'r')
        return [word.strip() for word in file.readlines()]
    except:
        return []

def save_word_list(words):
    with open(WORD_LIST, 'w') as file:
        file.write('\n'.join(words))

def create_re(green, yellow, black):
    gyb = []
    gyb.append(f".*[{black}]") # match if any word black character
    gyb.append(f"(?!{green})") # mismatch green characters
    dots='' # to specify position of yellow character
    for y in yellow:
        if y != '.':
            gyb.append(f"(?!.*[^{y}]*)") # match word without yellow
            gyb.append(f"^{dots}{y}") # match words with yellow at same spot
        dots=dots + '.' # add dot to position
    return "|".join(gyb)


def get_matches(green, yellow, black):
    pattern = create_re(green, yellow, black)
    return [word for word in word_list if not re.match(pattern, word)]

def pick_guess(matches):
    letter_counts = Counter(''.join(matches))
    letters = [letter for letter, _ in letter_counts.most_common()]
    for letter in letters:
        subset = [word for word in matches if letter in word]
        if subset:
            matches = subset
    return matches

def main():
    green_letters = 'ar'  #sys.argv[1]
    yellow_letters = 'so'  #sys.argv[2]
    black_letters = 'x'  #sys.argv[3]

    if len(sys.argv) > 3:
        green_letters = sys.argv[1]
        yellow_letters = sys.argv[2]
        black_letters = sys.argv[3]

    global word_list
    
    word_list = load_word_list(WORD_LIST)
    if len(word_list) == 0: # or sys.argv == 1:
        word_list = load_word_list(FULL_LIST)

    matches = get_matches(green_letters, yellow_letters, black_letters)
    save_word_list(matches)

    guess = pick_guess(matches)
    print(guess)

if __name__ == "__main__":
    main()
