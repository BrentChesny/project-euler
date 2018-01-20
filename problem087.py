from common import gen_primes

def solve():
    limit = 50000000
    primes_a = list(gen_primes(int(limit**0.5)))
    primes_b = list(gen_primes(int(limit**0.34)))
    primes_c = list(gen_primes(int(limit**0.25)))
    result = set()

    for a in primes_a:
        for b in primes_b:
            for c in primes_c:
                result.add(a**2 + b**3 + c**4)

    print len([x for x in result if x < limit])

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
