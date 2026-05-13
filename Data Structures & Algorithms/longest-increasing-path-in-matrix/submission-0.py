class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        mem = [[None for _ in range(m)] for _ in range(n)]

        def getNeighbours(i,j):
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    yield ni, nj

        self.global_max = 1

        def search(i,j):
            if mem[i][j]:
                return 
            
            neighbours = []
            for ni, nj in getNeighbours(i,j):
                if matrix[i][j] < matrix[ni][nj]:
                    neighbours.append((ni, nj))
            
            if not neighbours:
                local_max = 1
            else:   
                for ni, nj in neighbours:
                    search(ni, nj)

                local_max = 1 + max([mem[ni][nj] for ni, nj in neighbours])

            mem[i][j] = local_max
            if self.global_max < local_max:
                self.global_max = local_max

        for i in range(n):
            for j in range(m):
                if not mem[i][j]:
                    search(i, j) 
                    
        return self.global_max