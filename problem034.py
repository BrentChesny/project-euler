from math import factorial

def solve():
    total = 0
    facs = {n: factorial(n) for n in xrange(10)}

    for x in xrange(3, 10000000):
        if sum(facs[ord(c) - ord('0')] for c in str(x)) == x:
            total += x

    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
