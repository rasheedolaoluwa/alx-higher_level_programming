#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking
queens on an NxN chessboard, where N must be an integer greater
than or equal to 4. The script employs a recursive approach to
find all viable solutions, marking the board progressively to
avoid queen attacks. Each solution is represented as a list of
coordinates [row, column] for each queen's position.

Example usage:
    $ ./101-nqueens.py N

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing all possible solutions.
"""

import sys


def init_board(n):
    """Initialize an n x n sized chessboard with empty spaces."""
    board = []
    [board.append([' '] * n) for _ in range(n)]
    return board


def board_deepcopy(board):
    """Create a deep copy of the chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Extract the solution from the board in a list of [r, c] format."""
    return [[r, c] for r in range(len(board)) for c in
            range(len(board)) if board[r][c] == 'Q']


def xout(board, row, col):
    """Mark spaces where queens cannot be placed due to current queen."""
    for r in range(len(board)):
        for c in range(len(board)):
            if r == row or c == col or abs(r - row) == abs(c - col):
                if board[r][c] == ' ':
                    board[r][c] = 'x'


def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-queens problem by placing queens row by row."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == ' ':
            new_board = board_deepcopy(board)
            new_board[row][c] = 'Q'
            xout(new_board, row, c)
            solutions = recursive_solve(new_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)
