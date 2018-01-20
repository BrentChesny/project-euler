from fractions import Fraction

def simplify_naively(numerator, denominator):
    e, d = list(str(numerator)), list(str(denominator))

    for digit in xrange(10):
        x = str(digit)
        while x in e and x in d:
            e.remove(x)
            d.remove(x)

    e = int(''.join(e)) if e else 1
    d = int(''.join(d)) if d else 1
    return e, d

def solve():
    result = Fraction(1)
    for numerator in xrange(11, 100):
        for denominator in xrange(numerator + 1, 100):
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue
            e, d = simplify_naively(numerator, denominator)
            if e != numerator and numerator * d == denominator * e:
                result *= Fraction(numerator, denominator)
    return result.denominator

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
