from math import log10

def solve():
    pairs = [tuple(map(int, line.strip().split(','))) for line in open('resources/p099_base_exp.txt').readlines()]

    return max(range(len(pairs)), key=lambda i: pairs[i][1]*log10(pairs[i][0])) + 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
