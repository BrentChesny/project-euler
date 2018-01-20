def is_permutation(m, n):
    return sorted(str(m)) == sorted(str(n))

def solve():
    x = 1
    while True:
        if all(is_permutation(x, i*x) for i in xrange(2, 7)):
            return x
        x += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
