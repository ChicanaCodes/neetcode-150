def is_valid_sudoku(board: list[list[str]]) -> bool:
    '''
    Given a nested list of strings representing a sudoku board, check if each row, column, and 3 x 3 section unqiuely contains the numbers 1-9.
    Empty cells are represented by the character '.'.

    >>> is_valid_sudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]])
    True
    >>> is_valid_sudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]])
    False

    Edge Cases: 
    - Can the board be empty or not 9x9?
    - Can the board contain invalid characters?
    - Will the board always be a list of lists?
    - What should we return if the board is empty or not 9x9?
    - What should we return if the board contains invalid characters?
    - What should we return if the board is not a list of lists?
    
    Approach:
    1. Create a set to store the values we have seen.
    2. Iterate through each row and column of the board.
    3. For each value, check if it is a digit between 1-9.
    4. If it is, check if we have seen it before in the same row, column, or 3x3 section.
    5. If we have seen it before, return False.
    6. If we haven't seen it before, add it to the set.
    7. If we finish iterating through the board without finding any duplicates, return True.
    '''
    # check each row
    for row in board:
        seen = set()
        for val in row:
            if val != '.' and val in seen:
                return False
            else: 
                seen.add(val)
    # check each column
    for col in range(9):
        seen = set()
        for row in range(9):
            value = board[row][col]
            if value != '.' and value in seen:
                return False 
            seen.add(value)
    # check each 3x3 box
    for box_row in [0, 3, 6]:
        for box_col in [0, 3, 6]:
            seen = set()
            for i in range(3):
                for j in range(3):
                    value = board[box_row + i][box_col + j]
                    if value != '.' and value in seen:
                        return False
                    seen.add(value)
    return True
is_valid_sudoku([["1","2",".",".","3",".",".",".","."],
                 ["4",".",".","5",".",".",".",".","."],
                 [".","9","1",".",".",".",".",".","3"],
                 ["5",".",".",".","6",".",".",".","4"],
                 [".",".",".","8",".","3",".",".","5"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".",".",".",".",".",".","2",".","."],
                 [".",".",".","4","1","9",".",".","8"],
                 [".",".",".",".","8",".",".","7","9"]])



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed!")

# Time Complexity: O(n^2) - We iterate through each cell in the 9x9 board.
# Space Complexity: O(n) - We use a set to store the values we have seen