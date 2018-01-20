from common import totient, gen_primes

cache = {}

def chain_length(n):
    result = 2
    n -= 1
    while n > 1 and result < 26: # no point in computing chains longer than 25
        n = totient(n)
        result += 1
    return result
    
def solve():
    total = 0
    for p in gen_primes(40000000):
        if chain_length(p) == 25:
            total += p
    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
