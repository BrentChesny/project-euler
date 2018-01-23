from itertools import permutations, combinations, product

OPS = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y,
]

PARENTHESES = [
    lambda a, op1, b, op2, c, op3, d: op3(op2(op1(a, b), c), d),
    lambda a, op1, b, op2, c, op3, d: op3(op1(a, op2(b, c)), d),
    lambda a, op1, b, op2, c, op3, d: op1(a, op3(op2(b, c), d)),
    lambda a, op1, b, op2, c, op3, d: op1(a, op2(b, op3(c, d))),
    lambda a, op1, b, op2, c, op3, d: op2(op1(a, b), op3(c, d)),
]

def check_value(val, result):
    if val.is_integer() and val > 0:
        result.add(int(val))

def check_operators(digits):
    a, b, c, d = map(float, digits)
    result = set()
    
    for op1, op2, op3 in product(OPS, repeat=3):
        for par in PARENTHESES:
            try:
                check_value(par(a, op1, b, op2, c, op3, d), result)
            except ZeroDivisionError:
                pass
                
    return result

def solve():
    currentMax = None
    
    for digits in combinations(range(10), 4):
        result = set()
        
        for p in permutations(digits):
            result |= check_operators(p)

        i = 1
        while i in result:
            i += 1
            
        if currentMax == None or (i-1) > currentMax[0]:
            currentMax = (i-1, p)
                
    return ''.join(map(str, sorted(currentMax[1])))

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
