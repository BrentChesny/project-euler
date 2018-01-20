def solve():
    total = 0
    for x in xrange(2, 1000000):
        if sum((ord(c) - ord('0'))**5 for c in str(x)) == x:
            total += x
    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
