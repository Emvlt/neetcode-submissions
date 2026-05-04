class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nRows = len(grid)
        nCols = len(grid[0])

        def getNeighbors(i,j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < nRows and 0 <= nj < nCols:
                    yield ni, nj

        # Let's create a queue from all treasures
        queue = deque([])
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            (i,j) = queue.popleft()
            for ni, nj in getNeighbors(i,j):
                if grid[ni][nj] == 2147483647:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni, nj))