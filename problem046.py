from common import is_prime, gen_primes
from math import sqrt

def solve():
    x = 5

    while True:
        if not is_prime(x):
            for p in gen_primes(x):
                a = x - p
                if a % 2 == 0:
                    b = a / 2
                    b = sqrt(b)
                    if b.is_integer():
                        break
            else:
                return x
        x += 2

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
