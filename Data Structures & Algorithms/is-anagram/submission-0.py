from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        left  = defaultdict(int)
        right = defaultdict(int)
        for i in range(len(s)):
            left[s[i]]  += 1
            right[t[i]] += 1
        return left == right