class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
    
        l = 0
        r = len(cleaned) - 1

        def isPerfect(substring):
            return substring == substring[::-1]

        while l < r:                
            if cleaned[l] != cleaned[r]:
                return cleaned[l+1: r+1]==cleaned[l+1: r+1][::-1] or cleaned[l: r]==cleaned[l:r][::-1]

            l += 1
            r -= 1

        return True 