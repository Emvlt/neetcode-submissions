class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]

        for n in nums[1:]:
            curSum = max(n, n + curSum)
            maxSum = max(curSum, maxSum)
        return maxSum