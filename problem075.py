from common import gen_pythagorean_triples
from collections import defaultdict

L = 1500000

def solve():
    counts = defaultdict(int)
    
    for a, b, c in gen_pythagorean_triples(L):
        l = a + b + c
        if l <= L:
            counts[l] += 1

    return sum(1 for k, v in counts.iteritems() if v == 1)
        

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
