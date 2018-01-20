import string

TENS = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
SMALL = ['zero', 'one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
         'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen']


def nonzero(c, n, connect=''):
    return '' if n == 0 else connect + c + num_to_word(n)

def num_to_word(n):
    if n < 20:
        return SMALL[n]
    elif n < 100:
        a, b = divmod(n, 10)
        return TENS[a] + nonzero('-', b)
    elif n < 1000:
        a, b = divmod(n, 100)
        return SMALL[a] + ' hundred' + nonzero(' ', b, ' and')
    elif n == 1000:
        return 'one thousand'

def solve():
    return sum(len([c for c in num_to_word(x) if c in string.ascii_lowercase]) for x in range(1, 1001))

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
