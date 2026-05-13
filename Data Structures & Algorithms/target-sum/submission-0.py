class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # mem = {
        #     (index, 0),(index, 1)
        # }

        nWays = 0
        n = len(nums)

        def explore(index:int, current_sum:int):
            if index == n:
                return 1 if current_sum == target else 0

            value0 = current_sum + nums[index]
            value1 = current_sum - nums[index]    

            w0 = explore(index+1, value0)
            w1 = explore(index+1, value1)

            # # +
            # mem[(index, sign0)] = w0
            # # -
            # mem[(index, sign1)] = w1

            return w0 + w1 
        
        return explore(0, 0)