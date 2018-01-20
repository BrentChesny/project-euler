from itertools import permutations

def check_property(s):
    if int(s[1:4]) % 2 != 0:
        return False
    if int(s[2:5]) % 3 != 0:
        return False
    if int(s[3:6]) % 5 != 0:
        return False
    if int(s[4:7]) % 7 != 0:
        return False
    if int(s[5:8]) % 11 != 0:
        return False
    if int(s[6:9]) % 13 != 0:
        return False
    if int(s[7:10]) % 17 != 0:
        return False
    return True

def solve():
    result = []
    for p in permutations(range(0, 10)):
        x = ''.join(map(str, p))
        if check_property(x):
            result.append(int(x))
    return sum(result)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
