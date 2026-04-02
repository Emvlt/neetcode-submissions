class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            m = l + (r-l) // 2
            el = nums[m]
            if el == target:
                return m
            if el < target:
                l = m+1
            if el > target:
                r = m-1
        
        return -1