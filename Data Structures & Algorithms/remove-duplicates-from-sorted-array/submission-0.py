class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[n-1]
        w = 1
        r  = n-2
        while r >= 0:
            if nums[r] == curr:
                nums.pop(r)
            else:
                curr = nums[r]
                w += 1
            r -= 1

        return w
