from fractions import gcd

def solve():
    result = 0
    for i in xrange(1, 12001):
        for j in xrange(i/3, i):
            if gcd(j, i) == 1 and float(j)/i > 1.0/3 and float(j)/i < 0.5:
                result += 1
    return result

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
