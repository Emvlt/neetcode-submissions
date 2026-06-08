class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice  = prices[0]
        maxProfit = 0 

        for p in prices[1:]:
            if p < minPrice:
                minPrice = p

            currentProfit = p - minPrice
            maxProfit = max(maxProfit, currentProfit)

        return maxProfit