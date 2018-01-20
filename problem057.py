from fractions import Fraction

def solve():
    count = 0
    f = 0
    for i in xrange(1000):
        f = Fraction(1, 2 + f)
        if len(str((1 + f).numerator)) > len(str((1 + f).denominator)):
            count += 1
    return count

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
