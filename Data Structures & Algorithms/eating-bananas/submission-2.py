import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate, piles, h):
            return sum(math.ceil(p/rate) for p in piles) <= h

        l = 1
        r = max(piles)
        while l <= r:
            m = l + (r-l)//2
            if canEat(m, piles, h):
                r = m-1
            else:
                l = m+1

        return l
