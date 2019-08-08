import random


def magic_function(s):
    letter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    a = []
    for i in range(len(s)):
        if s[i] in letter:
            a.append(s[i])
    con_str = ''.join(a).split()
    b = []
    for i in range(len(con_str)):
        b.append(''.join(list(con_str[i])[::-1]))
    return ' '.join(random.sample(b, len(b)))


if __name__ == '__main__':
    print(magic_function('07neves 08thgie 2ytnewt 19neetenin'))
