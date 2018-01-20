from common import list_divisors

def d(n):
    return sum(list_divisors(n)) - n

def solve():
    amicable = []
    for a in xrange(10000):
        b = d(a)
        if d(b) == a and b != a:
            amicable.append(a)
    return sum(amicable)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
