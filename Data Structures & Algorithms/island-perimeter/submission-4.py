class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        mem = [[0 for _ in range(cols)] for _ in range(rows)]

        def getNeighbours(i, j):
            res = []
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= i+di < rows and 0 <= j+dj < cols and grid[i+di][j+dj]==1:
                    res.append((i+di, j+dj))
            return res

        def explore(i, j) -> int:
            mem[i][j] = 1

            def _helper(stack, p, i , j):
                neighbours = getNeighbours(i, j) 
                p += 4-len(neighbours)
                for ni, nj in neighbours:
                    if mem[ni][nj] == 0:
                        stack.append((ni,nj))
                        mem[ni][nj] = 1
                return stack, p 

            stack, p = _helper([], 0, i, j)

            while stack:
                i, j = stack.pop()
                
                stack, p = _helper(stack, p, i, j)
                

            return p

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and mem[i][j] == 0:
                    return explore(i, j) 