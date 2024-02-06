#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def print_solution(board):
    """
    Print the N Queens solution
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """
    Utility function to solve N Queens problem using backtracking
    """
    n = len(board)

    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1)
            board[i][col] = 0


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
