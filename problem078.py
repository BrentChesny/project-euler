from common import gen_generalized_pentagonal_nums
from collections import defaultdict

# Used resource: https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
def solve():
    p = defaultdict(int)
    p[0] = 1
    n = 1

    while True:
        i = 0
        for x in gen_generalized_pentagonal_nums(i):
            if x > n:
                break
            sign = 1 if i % 4 < 2 else -1
            p[n] += sign * p[n-x]
            i += 1
        if p[n] % 1000000 == 0:
            return n
        n += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
