from fractions import Fraction
from common import sum_of_digits

def coefficient(i):
    if i == 0:
        return 2
    elif i % 3 != 2:
        return 1
    else:
        return ((i / 3) + 1) * 2

def term(n, i=0):
    if i == n:
        return coefficient(i)
    else:
        return Fraction(1 , term(n, i+1) ) + coefficient(i)

def solve():
    return sum_of_digits(term(99).numerator)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
