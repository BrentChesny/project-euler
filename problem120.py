from collections import defaultdict

LIMIT = 1000
N = 2000

def solve():
    Dmin = defaultdict(list)
    Dplus = defaultdict(list)
    for a in xrange(3, LIMIT+1):
        for n in xrange(1, N+1):
            Dmin[a-1].append(pow(a-1, n, a**2))
            Dplus[a+1].append(pow(a+1, n, a**2))
            
    result = 0
    for a in xrange(3, LIMIT+1):
        result += max((x + y) % a**2 for x, y in zip(Dmin[a-1], Dplus[a+1]))
    return result
    
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
