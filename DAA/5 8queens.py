N = 8

board = [[0 for j in range(N)] for i in range(N)]

# Check whether queen can be placed
def is_safe(row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve(row):

    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


# Place first queen
board[0][0] = 1

if solve(1):
    print("Solution:")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
else:
    print("No solution exists")