class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])

        def explore(i, j):
            if i < 0 or j < 0 or i==nRows or j==nCols:
                return 

            if grid[i][j] == "0":
                return 

            grid[i][j] = "0"

            explore(i+1, j)
            explore(i-1, j)
            explore(i, j+1)
            explore(i, j-1)
            
        count = 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == "1":
                    count += 1
                    explore(i,j)

        return count