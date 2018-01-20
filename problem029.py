def solve():
    result = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            result.add(a**b)
    return len(result)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
