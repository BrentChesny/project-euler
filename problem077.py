from common import list_primes

N = 100

def solve():
    dp = [0] * (N+1)
    dp[0] = 1

    for i, p in enumerate(list_primes(N)):
        for j in xrange(p, N+1):
            dp[j] += dp[j-p]

    return [i for i, num_ways in enumerate(dp) if num_ways > 5000][0]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
