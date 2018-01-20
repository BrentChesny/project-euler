from common import Memoize
import operator

@Memoize
def chain_length(n):
    if n == 1:
        return 1
    else:
        return 1 + chain_length(n/2 if n % 2 == 0 else 3*n+1)

def solve():
    lengths = {x: chain_length(x) for x in xrange(1, 1000000)}

    return max(lengths.iteritems(), key=operator.itemgetter(1))[0]


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
