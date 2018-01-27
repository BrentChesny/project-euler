from common import gen_primes

DIGITS = map(str, range(10))
PRIMES = set(gen_primes(1000000))

def check_prime(p):
    p = str(p)
    for d in set(p):
        replacements = [int(p.replace(d, new_d)) for new_d in DIGITS]
        replacements = filter(lambda x: len(str(x)) == len(p), replacements)
        replacements = filter(lambda x: x in PRIMES, replacements)
        if len(replacements) >= 8:
            return True

def solve():
    for p in gen_primes():
        if check_prime(p):
            return p

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
