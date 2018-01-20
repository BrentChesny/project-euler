from common import is_prime

def is_permutation(m, n):
    return sorted(str(m)) == sorted(str(n))

def solve():
    for x in xrange(1000, 3340):
        if is_prime(x) and is_prime(x+3330) and is_prime(x+6660) and \
            is_permutation(x, x+3330) and is_permutation(x, x+6660) and x != 1487:
            return str(x) + str(x+3330) + str(x+6660)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
