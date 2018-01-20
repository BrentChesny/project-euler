def solve():
    f1, f2 = 1, 1
    idx = 3
    while True:
        f2, f1 = f1 + f2, f2
        if len(str(f2)) >= 1000:
            return idx
        idx += 1


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
