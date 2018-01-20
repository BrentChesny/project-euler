from common import gen_primes

def truncate_left(x):
    x = str(x)
    for i in range(1, len(x)):
        yield int(x[i:])

def truncate_right(x):
    x = str(x)
    for i in range(1, len(x)):
        yield int(x[:-i])

def solve():
    result = []
    primes = set()

    for x in gen_primes():
        primes.add(x)
        if x <= 7:
            continue
        if all(y in primes for y in truncate_left(x)) and all(y in primes for y in truncate_right(x)):
            result.append(x)
            if len(result) == 11:
                break

    return sum(result)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
