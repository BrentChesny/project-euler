from decimal import Decimal, getcontext

def solve():
    getcontext().prec = 102

    total = 0
    for x in xrange(100):
        root = Decimal(x).sqrt()
        if len(str(root)) > 1:
            total += sum(int(c) for c in str(root)[:101] if c != '.')

    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
