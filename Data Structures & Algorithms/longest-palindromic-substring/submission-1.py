from functools import lru_cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        @lru_cache(None)
        def explore(substring):
            if substring == substring[::-1]:
                return substring

            left  = explore(substring[1:])
            right = explore(substring[:-1])
        
            return left if len(left) >= len(right) else right

        return explore(s)

        