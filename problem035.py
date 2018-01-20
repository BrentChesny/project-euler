from collections import deque
from common import gen_primes

def rotations(num):
    d = deque(str(num))
    for i in xrange(len(d)):
        yield int(''.join(map(d.rotate(-1), d)))

def solve():
    primes = set(gen_primes(1000000))

    return len([x for x in primes if all(y in primes for y in rotations(x))])

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
