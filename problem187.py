from common import list_primes

def solve():
    primes = list_primes(50000000)
    result = set()

    for p in primes:
        for q in primes:
            n = p * q
            if n > 100000000:
                break
            else:
                result.add(n)

    return len(result)


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
