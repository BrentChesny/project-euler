from common import gen_primes
from collections import defaultdict
import operator

def solve():
    primes = list(gen_primes(1000000))
    primes_ = set(primes)
    result = defaultdict(list)

    for i in xrange(len(primes)):
        s = 0
        l = 0
        for j in xrange(i, len(primes)):
            s += primes[j]
            l += 1
            if s in primes_:
                result[l].append(s)
            if s > 1000000:
                break

    return max(result.iteritems(), key=operator.itemgetter(0))[1][0]


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
