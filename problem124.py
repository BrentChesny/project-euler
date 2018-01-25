from common import list_prime_factors
from operator import mul

N = 100000
TARGET = 10000

def solve():
    rads = sorted([(reduce(mul, set(list_prime_factors(n)), 1), n) for n in xrange(1, N+1)])
        
    return rads[TARGET-1][1]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
