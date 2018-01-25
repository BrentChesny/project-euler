from common import gen_primes

TARGET = 1e10

def solve():
    for n, p in enumerate(gen_primes()):
        r = (pow(p-1, n+1, p**2) + pow(p+1, n+1, p**2)) % p**2
        if r > TARGET:
            return n+1
            
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
