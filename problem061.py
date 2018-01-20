def backtrack(chain, types, candidates):
    if len(chain) == 6:
        if chain[-1] % 100 == chain[0] / 100:
            return chain
        else:
            return False

    for t, s in candidates.items():
        if t not in types:
            for c in s:
                if c not in chain:
                    if not chain or c / 100 == chain[-1] % 100:
                        val = backtrack(chain + [c], types + [t], candidates)
                        if val:
                            return val


def solve():
    TRI, SQ, PENTA, HEXA, HEPTA, OCTA = range(3, 9)
    candidates = {
        TRI : set(filter(lambda x: 1000 <= x <= 9999, [n*(n+1)/2 for n in range(500)])),
        SQ : set(filter(lambda x: 1000 <= x <= 9999, [n*n for n in range(500)])),
        PENTA : set(filter(lambda x: 1000 <= x <= 9999, [n*(3*n-1)/2 for n in range(500)])),
        HEXA : set(filter(lambda x: 1000 <= x <= 9999, [n*(2*n-1) for n in range(500)])),
        HEPTA : set(filter(lambda x: 1000 <= x <= 9999, [n*(5*n-3)/2 for n in range(500)])),
        OCTA : set(filter(lambda x: 1000 <= x <= 9999, [n*(3*n-2) for n in range(500)])),
    }

    return sum(backtrack([], [], candidates))

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
