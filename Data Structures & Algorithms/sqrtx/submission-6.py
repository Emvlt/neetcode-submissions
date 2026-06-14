class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l = 0
        r = x // 2

        while l <= r:
            m = l + (r-l)//2
            s = m**2
            if s == x:
                return m
            elif s < x:
                l = m + 1
            else:
                r = m - 1

        return r
