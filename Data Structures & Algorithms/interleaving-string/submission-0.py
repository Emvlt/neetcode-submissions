class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3:
            return not s1 and not s2

        if len(s3) != len(s1) + len(s2):
            return False

        mem = {}
        n = len(s1)
        m = len(s2)

        def search(i,j):
            if i == n and j == m:
                return True

            if (i, j) in mem:
                return mem[(i, j)]

            res = False

            # Only go down the s1 path if there are chars left AND it matches s3
            if i < n and s1[i] == s3[i + j]:
                res = search(i + 1, j)

            # Only go down the s2 path if s1 didn't already work (or check both)
            if not res and j < m and s2[j] == s3[i + j]:
                res = search(i, j + 1)

            mem[(i, j)] = res

            return mem[(i, j)] 

        return search(0,0)