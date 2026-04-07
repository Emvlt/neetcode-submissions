class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        bp = prices[0]
        for i in range(1, len(prices)):
            c = max(p, prices[i] - bp)
            if p < c:
                p = c
            bp = min(bp, prices[i])
        return p