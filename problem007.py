from common import gen_primes

def solve():
    count = 1
    for prime in gen_primes():
        if count == 10001:
            return prime
        count += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
