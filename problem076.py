def solve():
    dp = [0] * 101
    dp[0] = 1

    for i in xrange(1, 100):
        for j in xrange(i, 101):
            dp[j] += dp[j-i ]

    return dp[-1]

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
