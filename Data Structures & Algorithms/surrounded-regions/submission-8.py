class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        connected = set()

        def getNeighbours(i,j):
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < rows and 0 <= nj < cols: 
                    yield ni, nj

        def search(i,j):
            if board[i][j] == 'X':
                return 

            if (i,j) in connected:
                return

            connected.add((i,j))
            for ni, nj in getNeighbours(i,j):
                search(ni,nj)

        for i in range(rows):
            search(i, 0)
            search(i, cols-1)

        for j in range(cols):
            search(0, j)
            search(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in connected:
                    board[i][j] = 'X'