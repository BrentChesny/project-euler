def coin_change(coins, cents):
    dp = [[1] * (cents+1) for _ in xrange(len(coins))]
    for i in xrange(1, len(coins)):
        for j in xrange(1, cents+1):
            dp[i][j] = dp[i-1][j]
            if j - coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    return dp[-1][-1]

def solve():
    return coin_change([1, 2, 5, 10, 20, 50, 100, 200], 200)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
