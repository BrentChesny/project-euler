from common import gen_pentagonal_nums, gen_hexagonal_nums, gen_triangle_nums

def solve():
    pentagonals = set(gen_pentagonal_nums(1000000))
    hexagonals = set(gen_hexagonal_nums(1000000))

    for x in gen_triangle_nums():
        if x in pentagonals and x in hexagonals and x > 40755:
            return x

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
