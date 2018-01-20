import operator

def recurring_cycle_length(d):
    seen = [1]
    remainder = 1
    while True:
        remainder = (remainder * 10) % d
        if remainder == 0:
            return 0
        if remainder in seen:
            return len(seen) - seen.index(remainder)
        else:
            seen.append(remainder)

def solve():
    for d in xrange(2, 11):
        print d, recurring_cycle_length(d)

    cycle_lengths = {d: recurring_cycle_length(d) for d in xrange(2, 1000)}

    return max(cycle_lengths.iteritems(), key=operator.itemgetter(1))[0]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
