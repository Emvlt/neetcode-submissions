class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        

        if m < n:
            outer = n
            inner = m
            t1 = text2
            t2 = text1
        else:
            outer = m 
            inner = n
            t1 = text1
            t2 = text2 

        mem = [[0 for _ in range(inner+1)] for _ in range(outer+1)]

        for i in range(outer):
            for j in range(inner):
                if t1[i] == t2[j]:
                    mem[i+1][j+1] = 1 + mem[i][j]
                else:
                    mem[i+1][j+1] = max(mem[i][j+1], mem[i+1][j])

        return mem[-1][-1]
        