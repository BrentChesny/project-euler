from common import is_prime

def solve():
    total = 1
    primes = 0
    for i in xrange(3, 100000, 2):
        for j in xrange(4):
            x = i * i - (i - 1) * j
            if is_prime(x):
                primes += 1
            total += 1

        if float(primes) / float(total) < 0.10:
            return i

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
