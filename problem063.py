def solve():
    result = []
    n = 1
    while len(str(9**n)) >= n:
        for d in xrange(1, 10):
            x = d**n
            if len(str(x)) == n:
                result.append(x)
        n += 1

    return len(result)


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
