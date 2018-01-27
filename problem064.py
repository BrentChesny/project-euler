from math import sqrt

N = 10001

def period(x):
    history = []

    i = 0
    a = int(sqrt(x))
    b = 1
    c = a

    while True:
        history.append((a, b, c))

        b = (x - c*c) / b
        a = 0
        while c - b > -sqrt(x):
            c -= b
            a += 1
        c = abs(c)
        if (a, b, c) in history:
            j = history.index((a, b, c))
            return i - j + 1
        i += 1

def solve():
    result = 0
    for x in xrange(2, N):
        if sqrt(x).is_integer():
            continue
        if period(x) % 2 == 1:
            result += 1
    return result

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
