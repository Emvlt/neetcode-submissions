class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            # If middle is less than or equal to right, min is at m or to the left
            else:
                r = m
                
        return nums[l]