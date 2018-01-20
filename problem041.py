from itertools import permutations
from common import MillerRabin

def solve():
    mr = MillerRabin()
    result = []

    for n in xrange(1, 10):
        for p in permutations(range(1, n+1)):
            x = int(''.join(map(str, p)))
            if mr.is_prime(x):
                result.append(x)

    return max(result)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
