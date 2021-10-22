board = [
        [0, 0, 0, 0, 0, 7, 0, 0, 1],
        [9, 3, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 6, 7, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        [1, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 3, 9, 4, 0, 8, 6, 0],
        [3, 9, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 9, 0, 5],
        [5, 0, 4, 2, 6, 0, 0, 0, 0],
    ]


def print_board(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            print(str(bo[i][j]) + " ", end="")
            if j == 2 or j == 5:
                print(" | ", end="")
        print("\n")
        if i == 2 or i == 5:
            print("- - - - - - - - - - - -")


def find_empty(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            if bo[i][j] == 0:
                return [i, j]
    return False


def valid(bo, pos, num):
    for j in range(0, 9):
        if bo[pos[0]][j] == num:
            return False
    for i in range(0, 9):
        if bo[i][pos[1]] == num:
            return False
    box_i = pos[0] // 3
    box_j = pos[1] // 3
    for i in range(box_i*3, (box_i*3)+3):
        for j in range(box_j * 3, (box_j * 3) + 3):
            if bo[i][j] == num:
                return False
    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True

    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, [row, col], i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


print_board(board)
solve(board)
print("____________________________")
print_board(board)
