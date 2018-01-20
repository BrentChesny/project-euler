from common import is_pandigital

def solve():
    result = []

    for x in xrange(1, 100000):
        s = ''
        for y in xrange(1, 11):
            s += str(x*y)
            if y > 1 and is_pandigital(s):
                result.append(int(s))

    return max(result)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
