class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRowValid(board, rowIndex) -> bool:
            temp = set()
            for col in board[rowIndex]:
                if col != '.':
                    if col in temp:
                        return False
                    temp.add(col)

            return True

        def isColValid(board, colIndex) -> bool:
            temp = set()
            for row in range(9):
                val = board[row][colIndex]
                if val != '.':
                    if val in temp:
                        return False
                    temp.add(val) 
            return True

        def isSquareValid(board, i, j) -> bool:
            row_indices = [3*i, 3*i+1, 3*i+2]
            col_indices = [3*j, 3*j+1, 3*j+2]
            temp = set()
            for r_index in row_indices:
                for c_index in col_indices:
                    val = board[r_index][c_index]
                    if val != '.':
                        if val in temp:
                            return False
                        temp.add(val)
            return True

        isRowsValid = all([isRowValid(board, i) for i in range(9)])
        isColsValid = all([isColValid(board, i) for i in range(9)])
        isSquaresValid = all([isSquareValid(board, i,j) for i in range(3) for j in range(3)])
        return isRowsValid and isColsValid and isSquaresValid
        
