class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        BestSum = -1000
        currentSum = 0

        for n in nums:
            currentSum = max(n, n+currentSum)
            BestSum = max(currentSum, BestSum)

        return BestSum