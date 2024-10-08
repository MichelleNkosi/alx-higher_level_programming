#!/usr/bin/python3
import sys

def print_solutions(solutions):
    """Print the solutions in the desired format."""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the row and upper diagonals
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n, solutions):
    """Use backtracking to solve the N queens problem."""
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0  # backtrack

def nqueens(n):
    """Set up the board and initiate the solving process."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)
    print_solutions(solutions)
