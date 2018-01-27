def same_row(i, j):
    return i/9 == j/9

def same_col(i, j):
    return (i-j) % 9 == 0

def same_block(i, j):
    return i/27 == j/27 and i%9/3 == j%9/3

def solve_sudoku(puzzle):
    i = puzzle.find('0')
    if i == -1:
        return puzzle

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(puzzle[j])

    for m in '123456789':
        if m not in excluded_numbers:
            solution = solve_sudoku(puzzle[:i] + m + puzzle[i+1:])
            if solution:
                return solution

def solve():
    result = 0
    with open('resources/p096_sudoku.txt') as f:
        for _ in xrange(50):
            _ = f.readline()
            sudoku = ''
            for _ in xrange(9):
                sudoku += f.readline().strip()
            solved = solve_sudoku(sudoku)
            result += int(solved[:3])
    return result


def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
