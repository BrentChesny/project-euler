from math import factorial
from common import Memoize

FACS = {n: factorial(n) for n in xrange(10)}

def chain_length(x):
    seen = set()
    while x not in seen:
        seen.add(x)
        x = digit_factorial_sum(x)
    return len(seen)

@Memoize
def digit_factorial_sum(n):
    s = 0
    while n:
        s += FACS[n % 10]
        n //= 10
    return s

def solve():
    return sum(1 for x in xrange(1000000) if chain_length(x) == 60)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
