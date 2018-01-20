def solve():
    numerals = map(lambda l: l.strip(), open('resources/p089_roman.txt').readlines())
        
    minimal_numerals = []
    for numeral in numerals:
        numeral = numeral.replace('VIIII', 'IX')
        numeral = numeral.replace('IIII', 'IV')
        numeral = numeral.replace('LXXXX', 'XC')
        numeral = numeral.replace('XXXX', 'XL')
        numeral = numeral.replace('DCCCC', 'CM')
        numeral = numeral.replace('CCCC', 'CD')
        minimal_numerals.append(numeral)
    
    return sum(map(len, numerals)) - sum(map(len, minimal_numerals))
    
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
