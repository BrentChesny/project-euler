from itertools import product
from math import sqrt

N = 50

def eq(a, b):
    return abs(a-b) < 1e-8

def is_right_triangle(d1, d2, d3):
    if eq(d1*d1 + d2*d2, d3*d3) or eq(d2*d2 + d3*d3, d1*d1) or eq(d1*d1 + d3*d3, d2*d2):
        return True
    return False

def solve():
    result = 0
    for x1, y1, x2, y2 in product(range(N+1), repeat=4):
        if x1 == y1 == 0 or x2 == y2 == 0 or (x1 == x2 and y1 == y2):
            continue
        d1 = sqrt(x1*x1 + y1*y1)
        d2 = sqrt(x2*x2 + y2*y2)
        d3 = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
        if is_right_triangle(d1, d2, d3):
            result += 1
    return result/2

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
