from common import gen_primes

def solve():
    total = 0
    for prime in gen_primes():
        if prime > 2000000:
            break
        total += prime
    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
