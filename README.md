# Sudoku Solver

This is a Python implementation of a Sudoku solver using the backtracking algorithm. The solver solves a partially filled Sudoku puzzle by trying out possible values in each empty space while adhering to Sudoku rules: each row, each column, and each 3x3 block must contain the digits 1 through 9 without repetition.

## Table of Contents

- [Introduction](#introduction)
- [Functions](#functions)
  - [next_empty_block()](#next_empty_block)
  - [is_valid()](#is_valid)
  - [sudoku_solver()](#sudoku_solver)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Introduction

The `sudoku_solver` function uses backtracking to find the solution to a given Sudoku puzzle. It starts by finding the next empty block (represented by 0), guesses a number for it, and checks if the guess is valid. If valid, it proceeds to the next empty block. If no valid guesses are found, it backtracks and tries a different guess.

## Functions

### `next_empty_block(board)`
Finds the next empty block on the Sudoku board.

#### Parameters:
- `board`: A 2D list (9x9) representing the Sudoku grid.

#### Returns:
- A tuple `(row, col)` representing the coordinates of the next empty space (0).
- `(None, None)` if no empty spaces are left.

### `is_valid(board, guess, row, col)`
Checks if a guessed number is valid at a given position on the board.

#### Parameters:
- `board`: The Sudoku board.
- `guess`: The number being guessed (between 1 and 9).
- `row`: The row index of the guessed position.
- `col`: The column index of the guessed position.

#### Returns:
- `True` if the guess is valid.
- `False` if the guess is invalid.

### `sudoku_solver(board)`
Solves the Sudoku puzzle using the backtracking algorithm.

#### Parameters:
- `board`: A 2D list representing the Sudoku grid.

#### Returns:
- A solved Sudoku board if a solution is found.
- A message `"There is no solution to this table"` if no solution exists.

## Usage

To use the Sudoku solver, define a 9x9 grid where empty spaces are represented by `0` and pass it to the `sudoku_solver` function.

Example:

```python
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_board = sudoku_solver(board)
print(solved_board)
