import string
import random


def magic_function(s):
    s = s.split()
    for i, word in enumerate(s):
        for letter in word:
            if letter not in string.ascii_letters:
                word = word.replace(letter, '')
        s[i] = word[::-1]
    return ' '.join(random.sample(s, len(s)))


if __name__ == '__main__':
    print(magic_function('5ADadc1!!! s6d2,./ dv6/v3'))
