def solve():
    before = set()    
    digits = set()
    
    for line in open('resources/p079_keylog.txt'):
        d1, d2, d3 = map(int, line.strip())
        digits.add(d1)
        digits.add(d2)
        digits.add(d3)
        before.add((d1, d2))
        before.add((d2, d3))
        before.add((d1, d3))
    
    digits = sorted(digits, cmp=lambda x,y: -1 if (x,y) in before else 1) 
               
    return ''.join(map(str, digits))
        
        
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
