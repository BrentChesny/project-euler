def solve():
    sum_of_sq = sum(n*n for n in range(1, 101))
    sq_of_sum = sum(range(1, 101))
    sq_of_sum *= sq_of_sum

    return sq_of_sum - sum_of_sq

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
