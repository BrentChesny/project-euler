from itertools import *
import string

def solve():
    cipher = map(int, open('resources/p059_cipher.txt').read().strip().split(','))

    for key in product(map(ord, string.ascii_lowercase), repeat=3):
        plaintext = ''
        for c, k in zip(cipher, cycle(key)):
            plaintext += chr(c ^ k)

        # Run this simple test and identify the correct plaintext
        #
        # if 'the' in plaintext and 'an' in plaintext:
        #     print key, plaintext[:100]

        if 'The Gospel of John' in plaintext:
            return sum([ord(c) for c in plaintext])

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
