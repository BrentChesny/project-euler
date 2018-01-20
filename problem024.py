from itertools import permutations

def solve():
    i = 1
    for p in permutations('0123456789'):
        if i == 1000000:
            return ''.join(p)
        i += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
