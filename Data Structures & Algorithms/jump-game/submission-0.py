class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_reachable = 0
    
        for i, jump in enumerate(nums):
            if i > furthest_reachable:
                return False
            
            furthest_reachable = max(furthest_reachable, i + jump)
            
            if furthest_reachable >= len(nums) - 1:
                return True
                
        return True
    
