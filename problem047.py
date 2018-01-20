from common import list_prime_factors

def solve():
    count = 0
    factors = {}
    x = 2

    while True:
        f = set(list_prime_factors(x))
        factors[x] = f
        if len(f) == 4:
            count += 1
            if count == 4:
                return x - 3
        else:
            count = 0
        x += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
