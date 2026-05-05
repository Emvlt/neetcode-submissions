class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        nRows = len(heights)
        nCols = len(heights[0])
        pcf = set()
        atl = set()

        def getNeighbours(i,j):
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < nRows and 0 <= nj < nCols:
                    yield ni, nj

        def search(i, j, current_set:set):
            current_set.add((i,j))
            for ni, nj in getNeighbours(i,j):
                if (ni,nj) not in current_set and heights[i][j] <= heights[ni][nj]:
                    search(ni, nj, current_set)

        for c in range(nCols):
            search(0, c, pcf)           # Top -> Pacific
            search(nRows - 1, c, atl)   # Bottom -> Atlantic

        for r in range(nRows):
            search(r, 0, pcf)           # Left -> Pacific
            search(r, nCols - 1, atl)   # Right -> Atlantic
                    
        return [list(cell) for cell in pcf.intersection(atl)]