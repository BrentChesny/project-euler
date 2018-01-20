from common import list_divisors

def is_abundant(n):
    return sum(list_divisors(n)) - n > n

def solve():
    abundant = [x for x in xrange(1, 28123) if is_abundant(x)]
    nums = set(range(1, 28123))
    for x in abundant:
        for y in abundant:
            if x + y < 28123 and x + y in nums:
                nums.remove(x + y)
    return sum(nums)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
