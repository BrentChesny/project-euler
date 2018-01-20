from common import gen_triangle_nums
import string

def solve():
    words = open('resources/p042_words.txt').readline().strip().split(',')
    words = map(lambda x: x[1:-1], words)

    triangles = set(gen_triangle_nums(1000))

    total = 0
    for word in words:
        word_value = sum(string.ascii_uppercase.index(c)+1 for c in word)
        if word_value in triangles:
            total += 1

    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
