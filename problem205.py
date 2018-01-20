from itertools import product

def calculate_pyramid_chances():
    pyramid_chances = [0] * 37

    total_throws = 0
    for throw in product(range(1, 5), repeat=9):
        pyramid_chances[sum(throw)] += 1
        total_throws += 1

    return [p/float(total_throws) for p in pyramid_chances]

def calculate_cube_chances():
    cube_chances = [0] * 37

    total_throws = 0
    for throw in product(range(1, 7), repeat=6):
        cube_chances[sum(throw)] += 1
        total_throws += 1

    return [p/float(total_throws) for p in cube_chances]

def solve():
    pyramid_chances = calculate_pyramid_chances()
    cube_chances = calculate_cube_chances()
    result = 0

    for i, pc in enumerate(pyramid_chances):
        for j, cc in enumerate(cube_chances):
            if i > j:
                result += pc * cc

    return round(result, 7)


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
