class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}

        n = len(prices)

        def search(i:int, buying:int):
            if i >= n:
                return 0
                
            if (i, buying) in mem:
                return mem[(i, buying)]

            # I have a coin
            if buying:
                res = max(
                    search(i+1, False) - prices[i], # I buy
                    search(i+1, True)  # I skip
                )

            else:
                res = max(
                    search(i+2, True) + prices[i], # I Sell
                    search(i+1, False)  # I skip
                )

            mem[(i, buying)] = res

            return res

        return search(0, True)
