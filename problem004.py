def solve():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            x = i*j
            if str(x) == str(x)[::-1]:
                palindromes.append(x)
    return max(palindromes)

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
