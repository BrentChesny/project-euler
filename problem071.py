from fractions import gcd

def solve():
    ref = 3.0/7
    e = 2
    d = 5
    
    for i in xrange(1, 1000001):
        for j in xrange((i/d)*e, (i*3)/7+1):
            if gcd(j, i) == 1:
                if float(j)/i < ref and float(j)/i > float(e)/d:
                    e, d = j, i
    return e

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
