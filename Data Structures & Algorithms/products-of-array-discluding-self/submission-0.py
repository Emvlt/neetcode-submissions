class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mem = [nums[0] for i in range(len(nums))]
        mem[0] = 1
        n = len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                mem[j] *= nums[i]
            for k in range(i+1, n):
                mem[k] *= nums[i]
        return mem