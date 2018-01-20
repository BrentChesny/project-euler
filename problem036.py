def solve():
    total = 0

    for x in xrange(1000000):
        if str(x) == str(x)[::-1] and bin(x)[2:] == bin(x)[:1:-1]:
            total += x

    return total

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
