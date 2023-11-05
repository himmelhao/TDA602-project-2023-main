# generate typo for the dependencies on the place next to the origional word

import random
import typos
from typos import typos

delimiter_list = [' ', '.', '-', '_']

# Define a function to generate random typos

def generate_typo(word):
    if "-" not in word:
        typo_type = random.choice(
            [omitted_letter_typo, repeated_letter_typo, swapped_letter_typo, common_typos_typo])
    else:
        typo_type = random.choice([omitted_letter_typo, repeated_letter_typo,
                                  swapped_letter_typo, common_typos_typo, swapped_words_typo])
    return typo_type(word)


def omitted_letter_typo(word):
    index = random.randint(0, len(word) - 1)
    return word[:index] + word[index+1:]


def repeated_letter_typo(word):
    index = random.randint(0, len(word) - 1)
    return word[:index] + word[index] + word[index:]


def swapped_letter_typo(word):
    if len(word) <= 1:
        return word
    idx1 = random.randint(0, len(word) - 2)
    idx2 = idx1 + 1
    return word[:idx1] + word[idx2] + word[idx1] + word[idx2+1:]


def common_typos_typo(word):
    index = random.randint(0, len(word) - 1)
    letter = word[index]
    if letter.lower() in typos:
        new_letter = random.choice(typos[letter.lower()])
        new_word = word[:index] + new_letter + word[index+1:]
        return new_word
    else:
        return word


def swapped_words_typo(word):
    delimiter_list = [' ', '-', '_', '.']  # Example delimiter list
    for delimiter in delimiter_list:
        str_list = word.replace(delimiter, '-')
    words = str_list.split('-')
    if len(words) <= 1:
        return word
    idx1 = random.randint(0, len(words) - 2)
    words[idx1], words[idx1+1] = words[idx1+1], words[idx1]
    deli = random.choice(delimiter_list)
    return ('-').join(words)
