class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])        
        
        def getNeighbors(i,j):
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < nRows and 0 <= nj < nCols:
                    yield ni, nj 

        queue = deque()
        fresh = set()

        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    queue.append((i,j))

        if not fresh:
            return 0

        level = -1
        while queue:
            length = len(queue)
            for i in range(length):
                i, j = queue.popleft()

                for ni, nj in getNeighbors(i,j):
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2 
                        fresh.remove((ni, nj))
                        queue.append((ni,nj))

            level += 1

        return -1 if fresh else level

