TARGET = 30

def solve():
    nums = set()
    for b in xrange(2, 1000):
        for e in xrange(1, 50):
            n = b**e
            if sum(map(int, str(n))) == b and n >= 10:
                nums.add(n)
    
    return sorted(nums)[TARGET-1]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
