import operator

def number_of_solutions(p):
    count = 0
    for a in xrange(1, p):
        for b in xrange(a, p-a):
            c = p - a - b
            if a*a + b*b == c*c:
                count += 1
    return count

def solve():
    result = {p: number_of_solutions(p) for p in xrange(1001)}
    return max(result.iteritems(), key=operator.itemgetter(1))[0]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
