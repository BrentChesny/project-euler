N = 1000000

def solve():
    result = 0
    for inner in xrange(1, N/4 + 2):
        for outer in xrange(inner + 2, N/4 + 2, 2):
            if outer*outer - inner*inner > N:
                break
            result += 1
    return result

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
