from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        @lru_cache
        def decode(i):
            if i == n:
                return 1

            if s[i] == '0':
                return 0

            res = decode(i+1)

            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                res += decode(i+2)

            return res

        return decode(0)
