class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        nRows = len(grid)
        nCols = len(grid[0])

        def explore(i,j) -> int:
            if i==nRows or j==nCols or i<0 or j<0:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            s = explore(i-1,j)
            n = explore(i+1,j)
            e = explore(i,j+1)
            w = explore(i,j-1)

            return 1+s+n+e+w
        

        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    current_area = explore(i,j)
                    if max_area < current_area:
                        max_area = current_area

        return max_area 