cache = {}
    
def chain_end(num):
    global cache
    n = num
    while n != 89 and n != 1:
        if n in cache:
            return cache[n]
        s = 0
        while n:
            s += (n % 10) ** 2
            n //= 10
        n = s
    cache[num] = n
    return n

def solve():
    count = 0
    for num in xrange(1, 10000001):
        if chain_end(num) == 89:
            count += 1
    return count
        
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
