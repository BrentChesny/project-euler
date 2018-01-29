from collections import defaultdict

N = 1000000

def solve():
    solution_counts = defaultdict(int)
    for inner in xrange(1, N/4 + 2):
        for outer in xrange(inner + 2, N/4 + 2, 2):
            if outer*outer - inner*inner > N:
                break
            solution_counts[outer*outer - inner*inner] += 1

    return sum(1 for _, v in solution_counts.iteritems() if 0 < v <= 10)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
