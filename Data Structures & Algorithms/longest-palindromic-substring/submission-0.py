from functools import lru_cache

class Solution:
    def longestPalindrome(self, s: str) -> str:

        @lru_cache(None)
        def explore(current_s:str) -> bool:
            if current_s == current_s[::-1]:
                return current_s

            res_left = explore(current_s[1:])
        
            # Check s[:-1]
            res_right = explore(current_s[:-1])

            # Return whichever is longer
            if len(res_left) >= len(res_right):
                return res_left
            return res_right

        return explore(s)
        

        