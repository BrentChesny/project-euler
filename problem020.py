from math import factorial
from common import sum_of_digits

def solve():
    return sum_of_digits(factorial(100))

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
