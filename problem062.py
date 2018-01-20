from collections import defaultdict

def solve():
    d = defaultdict(list)

    for x in xrange(100000):
        d[tuple(sorted(str(x**3)))].append(x)

    result = min([min(xs) for xs in d.itervalues() if len(xs) == 5])

    return result**3

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
