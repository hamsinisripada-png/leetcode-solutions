class Solution:
    def solveSudoku(self, board):
        def is_valid(row, col, num):
            # Check row
            for c in range(9):
                if board[row][c] == num:
                    return False

            # Check column
            for r in range(9):
                if board[r][col] == num:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False

            return True

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":

                        for num in "123456789":
                            if is_valid(row, col, num):
                                board[row][col] = num

                                if backtrack():
                                    return True

                                board[row][col] = "."

                        return False

            return True

        backtrack()

"""
LeetCode 37 - Sudoku Solver
Difficulty: Hard

Approach:
- Use Backtracking to fill empty cells ('.') in the Sudoku board.
- For each empty cell, try placing digits from 1 to 9.
- Before placing a digit, check if it is valid according to Sudoku rules:
    1. The digit must not already exist in the same row.
    2. The digit must not already exist in the same column.
    3. The digit must not already exist in the corresponding 3x3 sub-grid.
- If a valid digit is found, place it and recursively solve the remaining board.
- If a dead end is reached, undo the placement (backtrack) and try another digit.
- Continue until the entire board is solved.

Time Complexity:
- Worst Case: O(9^(empty cells))
- In practice, much faster due to constraint pruning.

Space Complexity:
- O(empty cells) for recursion stack.
"""
