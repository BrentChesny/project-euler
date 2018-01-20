from common import gen_pentagonal_nums

def pentagonal(n):
    return n*(3*n-1)/2

def solve():
    pentagonals = set(gen_pentagonal_nums(1000000))
    n = 1
    done = False

    while not done:
        for d in xrange(n-1, 0, -1):
            p = pentagonal(n)
            x = pentagonal(n-d)

            if p-x in pentagonals and p+x in pentagonals:
                return abs(p-x)
        n += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
