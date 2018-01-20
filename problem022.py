import string

def solve():
    words = open('resources/p022_names.txt').readline().strip().split(',')
    words = sorted(map(lambda x: x[1:-1], words))

    total = 0
    for i, word in enumerate(words):
        word_value = sum(string.ascii_uppercase.index(c)+1 for c in word)
        total += (i+1) * word_value

    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
