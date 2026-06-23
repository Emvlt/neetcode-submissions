class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        mem = [[0 for _ in range(cols)] for _ in range(rows)]

        def getNeighbours(i, j):
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+di < rows and 0 <= j+dj < cols:
                    yield i+di, j+dj

        def explore(i, j):

            def helper(i, j):
                for ni, nj in getNeighbours(i, j):
                    if grid[ni][nj] == '1' and mem[ni][nj] == 0:
                        stack.append((ni, nj))

            mem[i][j] = 1

            stack = []
            helper(i, j)

            while stack:
                ni, nj = stack.pop()
                mem[ni][nj] = 1
                helper(ni, nj)            

        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and mem[i][j] == 0:
                    explore(i, j)
                    count += 1

        return count