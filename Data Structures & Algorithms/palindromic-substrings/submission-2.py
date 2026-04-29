from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0 
        def expand_and_count(l, r):
            count = 0
            # While we are inside the string and the characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1 # Move left pointer out
                r += 1 # Move right pointer out
            return count
            
        for i in range(len(s)):
            # Check for odd palindromes (center is at i)
            total_count += expand_and_count(i, i)
            # Check for even palindromes (center is between i and i+1)
            total_count += expand_and_count(i, i + 1)
            
        return total_count