class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def explore(i,j):
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    yield ni, nj
            

        def backtracking(i, j, index, indices:set):
            if board[i][j] == word[index] and index == len(word) -1:
                return True

            for ni, nj in explore(i,j):
                if (ni, nj) not in indices and board[ni][nj] == word[index+1]:
                    indices.add((ni,nj))
                    index += 1
                    res = backtracking(ni, nj, index, indices)
                    if res:
                        return True
                    indices.remove((ni,nj))
                    index -= 1

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    s = set([(i, j)])
                    res = backtracking(i, j, 0, s) 
                    if res:
                        return True

        return False

                           