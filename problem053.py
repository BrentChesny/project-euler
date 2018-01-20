from common import n_choose_k

def solve():
    total = 0
    for n in xrange(1, 101):
        for r in xrange(1, n+1):
            if n_choose_k(n, r) > 1000000:
                total += 1
    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
