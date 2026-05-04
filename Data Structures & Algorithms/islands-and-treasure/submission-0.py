class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nRows = len(grid)
        nCols = len(grid[0])
        visited = set()

        def getNeighbors(i,j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = i + di, j + dj
                if 0 <= nr < nRows and 0 <= nc < nCols:
                    yield nr, nc

        # Let's create a queue from all treasures
        treasures = []
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 0:
                    treasures.append((i,j))

        queue = deque(treasures)
        while queue:
            i,j = queue.popleft()
            
            for neighbor in getNeighbors(i,j):
                r, c = neighbor
                if grid[r][c] == 2147483647:
                    grid[r][c] = grid[i][j] + 1
                    queue.append((r,c))
