from common import list_primes, MillerRabin
from collections import defaultdict

LIMIT = 10000
N = 5

def do_first_pass():
    mr = MillerRabin()
    concatenates = defaultdict(bool)
    primes = list_primes(LIMIT)
    pairs = set()
    
    for i, p1 in enumerate(primes):
        for p2 in primes[i+1:]:
            if mr.is_prime(int(str(p1) + str(p2))) and mr.is_prime(int(str(p2) + str(p1))):
                pairs.add(frozenset([p1, p2]))
                concatenates[(p1, p2)] = True
                concatenates[(p2, p1)] = True
    
    return pairs, reduce(frozenset.union, pairs), concatenates

def do_ith_pass(i, n_sets, primes, concatenates):
    n_plus_one_sets = set()
    for ps in n_sets:
        for candidate in primes:
            for p in ps:
                if not concatenates[(candidate, p)] or not concatenates[(p, candidate)]:
                    break
            else:
                n_plus_one_sets.add(ps.union(set([candidate])))
    return n_plus_one_sets, reduce(frozenset.union, n_plus_one_sets)

def solve():
    n_sets, primes, concatenates = do_first_pass()
    
    for i in range(2, N):
        n_sets, primes = do_ith_pass(i, n_sets, primes, concatenates)
            
    return min(map(sum, n_sets))
                   

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
