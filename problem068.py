from itertools import permutations
from operator import itemgetter

# As an illustration of variable names:
#    A
#       F    B
#    J     G
# E    I H   C
#       D
      
def solve():
    result = []
    for a, b, c, d, e, f, g, h, i, j in permutations(range(1, 11)):
        if a + f + g == b + g + h == c + h + i == d + i + j == e + j + f:
            arms = [(a, f, g), (b, g, h), (c, h, i), (d, i, j), (e, j, f)]
            m = min([a, b, c, d, e])
            while arms[0][0] != m:
                arms = arms[1:] + [arms[0]]
            digit_number = ''.join(str(v) for arm in arms for v in arm)
            if len(digit_number) == 16:
                result.append(digit_number)
    return max(result)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
