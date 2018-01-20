from common import totient, gen_primes

LIMIT = 15499.0 / 94744

def solve():
    d = 1
    primes = []
    phi = None

    while True:
        for p in gen_primes():
            d *= p
            primes.append(p)
            phi = totient(d)
                        
            if phi / float(d-1) < LIMIT:
                if p > 2:
                    primes.pop()
                    d /= p
                    phi = totient(d)
                    break
                else:
                    return d
        
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
