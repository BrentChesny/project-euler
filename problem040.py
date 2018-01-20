def solve():
    s = ''
    i = 1
    while len(s) < 1000000:
        s += str(i)
        i += 1

    return reduce(lambda x, y: x*y, map(int, [s[0], s[9], s[99], s[999], s[9999], s[99999], s[999999]]), 1)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
