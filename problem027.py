from common import is_prime
from itertools import count
import operator

def check_equation(a, b):
    cnt = 0
    for n in count():
        if not is_prime(n*n + a*n + b):
            break
        cnt += 1
    return cnt

def solve():
    results = {}
    for a in xrange(-999, 1000):
        for b in xrange(-1000, 1001):
            results[(a,b)] = check_equation(a, b)

    ma, mb = max(results.iteritems(), key=operator.itemgetter(1))[0]
    return ma * mb

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
