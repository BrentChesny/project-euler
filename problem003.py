def solve():
    n = 600851475143
    factor = 2
    factors = []

    while factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n /= factor
        else:
            factor += 1

    return factors[-1]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
