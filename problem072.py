from common import totient

def solve():
    return sum(totient(i) for i in xrange(2, 1000001))

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
