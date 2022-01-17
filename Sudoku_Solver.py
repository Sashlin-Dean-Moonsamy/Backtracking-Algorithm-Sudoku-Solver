# Define function That finds next empty block on board
def next_empty_block(board):

    # Create for loop to loop over board and fine an empty position indicated by 0 and return positions
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c

    # If there are no empty spaces return None
    return None, None


# Define a function that would act as validator
def is_valid(board, guess, row, col):

    # If guess in row return false
    if guess in board[row]:
        return False

    # Loop through rows to assign column values to list
    col_values = [board[i][col] for i in range(9)]

    # If guess in column return false
    if guess in col_values:
        return False

    # Find start of 3 X 3 block row and column
    row_start = (row // 3) * 3
    col_start = (row // 3) * 3

    # Loop through block to validate block. If guess is in block return True else return False
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False

    return True


# Define a sudoku_solver function
def sudoku_solver(board):

    # Assign values of row and column by calling next_empty_block() function
    row, col = next_empty_block(board)

    # If there are no more empty spaces return True
    if row is None:
        return True

    # Create for loop to provide guess for empty space
    for guess in range(1, 10):

        # Use validator to determine if guess is valid
        if is_valid(board, guess, row, col):

            # If guess is valid assign guess to empty position
            board[row][col] = guess

            # Recursively call sudoku_solver() function to solve for next empty space if there are any
            if sudoku_solver(board):
                return board

        # If answer not valid backtrack by resetting empty space and trying again7
        board[row][col] = 0

    # If there no solution return appropriate statement
    return "\n\t\tThere is no solution to this table"
