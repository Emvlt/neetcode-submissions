class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        mem = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    mem[i+1][j+1] = 1 + mem[i][j]
                else:
                    mem[i+1][j+1] = max(mem[i][j+1], mem[i+1][j])

        return mem[-1][-1]
        