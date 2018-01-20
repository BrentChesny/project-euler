from math import sqrt

def check(n):
    return str(n)[::2] == '1234567890'

def solve():
    minroot = int(sqrt(1020304050607080900))
    maxroot = int(sqrt(1929394959697989990)) + 1
    
    for x in xrange(maxroot, minroot, -1):
        if check(x*x):
            return x

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
