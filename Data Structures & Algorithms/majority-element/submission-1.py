class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1

        for n in nums[1:]:
            if count == 0:
                res = n
                count = 0

            
            count += (1 if n == res else -1)

        return res