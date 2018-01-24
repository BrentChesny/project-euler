from common import gen_divisors

LIMIT = 1000000
SUMS_OF_FACTORS = {n: sum(gen_divisors(n)) - n for n in xrange(LIMIT)}

def chain(n):
    x = n
    seen = set()
    while x not in seen:
        if x > LIMIT:
            return None
        seen.add(x)
        x = SUMS_OF_FACTORS[x]
    return seen if x == n else None
        
def solve():
    longest_chain = set()
    
    for n in xrange(2, LIMIT):
        c = chain(n)
        if c and len(c) > len(longest_chain):
            longest_chain = c
    
    return min(longest_chain)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
