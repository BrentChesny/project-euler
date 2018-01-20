def solve():
    for a in xrange(1, 999):
        for b in xrange(a, 999):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                return a*b*c

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
