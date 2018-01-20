def solve():
    return max(sum(map(int, str(a**b))) for a in xrange(100) for b in xrange(100))

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
