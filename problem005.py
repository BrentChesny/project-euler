def solve():
    divisors = range(11, 20)
    for x in xrange(20, 999999999, 20):
        if all(x % d == 0 for d in divisors):
            return x

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
