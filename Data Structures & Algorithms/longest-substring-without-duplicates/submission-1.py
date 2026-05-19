class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        charSet = set(s[0])

        l = 0

        res = 1

        for r in range(1, len(s)):
            while s[r] in charSet:
                print(r, l, charSet)                   
                charSet.remove(s[l])
                l += 1 

            charSet.add(s[r])
            res = max(res, r-l+1)

        return res
