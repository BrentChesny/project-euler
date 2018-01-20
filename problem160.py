N = 1000000000000

def factors(x, n):
    result = 0
    y = x
    while x < n:
        result += n / x
        x *= y
    return result
        
    
def f(n):
    return even(n) * odd(n) % 100000
    
def even(n):
    if n == 0:
        return 1
    else:
        return f(n / 2)
        
def odd(n):
    if n == 0:
        return 1
    else:
        return odd(n / 5) * coprime(n) % 100000
        
def coprime(n):
    n %= 100000
    result = 1
    for i in xrange(1, n + 1):
		if i % 2 != 0 and i % 5 != 0:
			result = i * result % 100000
    return result
    
def solve():
    twos = factors(2, N) - factors(5, N)
    return f(N) * pow(2, twos, 100000) % 100000
    

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
