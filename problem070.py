from common import totient, list_primes
import operator

def is_permutation(m, n):
    return sorted(str(m)) == sorted(str(n))

def solve():
    primes = list_primes(1000000)
    result = {}

    for x in primes[:300:-1]:
        for y in primes[300:]:
            n = x * y
            if n > 10000000:
                break
            phi = totient(n)
            if is_permutation(n, phi):
                result[n] = float(n)/phi

    return min(result.iteritems(), key=operator.itemgetter(1))[0]

def solve_slow():
    result = {}
    for n in xrange(2, 10000000):
        phi = totient(n)
        if is_permutation(n, phi):
            result[n] = float(n)/phi

    return min(result.iteritems(), key=operator.itemgetter(1))[0]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
