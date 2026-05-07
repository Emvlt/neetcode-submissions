class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0 for _ in range(n)] for _ in range(m)]

        mem[0] = [1 for i in range(n)]
        for i in range(m):
            mem[i][0] = 1

        def nPaths(i,j):
            if mem[i][j] != 0:
                return mem[i][j]

            mem[i][j] = nPaths(i-1,j) + nPaths(i, j-1)
            return mem[i][j]

        return nPaths(m-1, n-1)