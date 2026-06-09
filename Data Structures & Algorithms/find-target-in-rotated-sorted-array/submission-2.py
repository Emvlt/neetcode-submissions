class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_hinge(nums):
            l = 0 
            r = len(nums)-1

            while l < r:
                m = l + (r-l) // 2
                if nums[l] <= nums[m] <= nums[r]:
                    return l

                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        # Find hinge point
        hinge = find_hinge(nums)
        if nums[-1] == target:
            return len(nums)-1
        
        if nums[-1] < target:
            l = 0
            r = hinge -1
        else:
            l = hinge
            r = len(nums)-1

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1


        return -1