class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows = len(matrix)
        nCols = len(matrix[0])

        def _helper(index:int) -> (int, int):
            return divmod(index, nCols)
        
        l = 0
        r = nRows * nCols -1

        while l <= r:
            m = l + (r-l)//2
            i, j = _helper(m)

            if matrix[i][j] == target:
                return True

            elif matrix[i][j] < target:
                l = m + 1
            
            else:
                r = m - 1

        return False

