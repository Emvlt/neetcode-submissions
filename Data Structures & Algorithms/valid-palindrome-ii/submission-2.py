class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
    
        l = 0
        r = len(cleaned) - 1

        def isPerfect(substring):
            return substring == substring[::-1]

        while l < r:                
            if cleaned[l] != cleaned[r]:
                return isPerfect(cleaned[l+1: r+1]) or isPerfect(cleaned[l: r])

            l += 1
            r -= 1

        return True 