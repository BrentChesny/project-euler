def solve():
    total = 1
    for i in xrange(3, 1002, 2):
        for j in xrange(4):
            total += i * i - (i - 1) * j
    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
