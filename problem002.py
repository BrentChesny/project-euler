def solve():
    fib = [1, 2]
    while True:
        x = fib[-1] + fib[-2]
        if x > 4000000:
            break
        else:
            fib.append(x)
    return sum(x for x in fib if x % 2 == 0)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
