from common import list_divisors, gen_triangle_nums

def solve():
    for x in gen_triangle_nums():
        if len(list_divisors(x)) > 500:
            return x

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
