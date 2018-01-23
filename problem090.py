from itertools import combinations, product

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SQUARES = set([1, 4, 9, 16, 25, 36, 49, 64, 81])

def extend(s):
    extended = set(s)
    if 6 in s:
        extended.add(9)
    elif 9 in s:
        extended.add(6)        
    return extended

def solve():
    sets = [set(c) for c in combinations(DIGITS, 6)]

    result = 0
    for cube1, cube2 in combinations(sets, 2):
        c1 = extend(cube1)
        c2 = extend(cube2)
        numbers = set()
        for d1, d2 in product(c1, c2):
            numbers.add(d1 * 10 + d2)
            numbers.add(d2 * 10 + d1)
        if SQUARES.issubset(numbers):
            result += 1
            
    return result
        
            

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
