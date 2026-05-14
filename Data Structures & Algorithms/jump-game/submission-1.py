class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i, val in enumerate(nums):
            if i > furthest:
                return False
            
            jump = i+val
            furthest = max(furthest, jump) 

            if furthest >= len(nums)-1:
                return True
        
        return True
