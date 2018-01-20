from common import totient
import operator

def solve():
    result = {n: float(n)/totient(n) for n in xrange(2, 1000001)}
    return max(result.iteritems(), key=operator.itemgetter(1))[0]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
