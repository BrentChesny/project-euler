def is_bouncy(n):
    n = str(n)
    diffs = [int(a) - int(b) for a,b in zip(n, n[1:])]
    normalized_diffs = [d/abs(d) for d in diffs if d != 0]
    return abs(sum(normalized_diffs)) != len(normalized_diffs)

def solve():
    n = 1
    bouncy = 0
    while True:
        if is_bouncy(n):
            bouncy += 1
        if float(bouncy) / n >= 0.99:
            return n
        n += 1

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
