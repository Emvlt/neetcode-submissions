class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S%2 != 0:
            return False

        t = S//2

        dp = [False for i in range(t + 1)]
        dp[0] = True

        for num in nums:
            for j in range(t, num-1, -1):
                dp[j] = dp[j] or dp[j-num]

        return dp[-1]