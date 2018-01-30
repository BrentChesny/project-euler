def sign(p1, p2):
    return (-p2[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (-p2[1])

def origin_in_triangle(v1, v2, v3):
    b1 = sign(v1, v2) < 0
    b2 = sign(v2, v3) < 0
    b3 = sign(v3, v1) < 0
    return b1 == b2 == b3

def solve():
    result = 0
    for line in open('resources/p102_triangles.txt').readlines():
        coordinates = map(int, line.strip().split(','))
        v1 = coordinates[0], coordinates[1]
        v2 = coordinates[2], coordinates[3]
        v3 = coordinates[4], coordinates[5]
        if origin_in_triangle(v1, v2, v3):
            result += 1
    return result

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
