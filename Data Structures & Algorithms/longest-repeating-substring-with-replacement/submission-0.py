from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res  = 0
        l    = 0
        maxF = 1
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1 
            maxF = max(maxF, count[s[r]])

            while r-l+1 - maxF > k:
                count[s[l]] -=1
                l += 1
            res = max(res, r-l+1)
        return res