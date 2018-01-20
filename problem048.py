def solve():
    total = 0
    for x in xrange(1, 1001):
        total += x**x
    return total % 10000000000

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
