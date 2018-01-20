from common import is_pandigital

def solve():
    products = set()
    for p in xrange(10000):
        for x in xrange(2, int(p**0.5)):
            if p % x == 0 and is_pandigital('{}{}{}'.format(p, x, p/x)):
                products.add(p)
    return sum(products)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
