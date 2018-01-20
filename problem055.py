def solve():
    count = 0
    for x in xrange(1, 10001):
        for _ in xrange(50):
            x += int(str(x)[::-1])
            if str(x) == str(x)[::-1]:
                break
        else:
            count += 1
    return count

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
