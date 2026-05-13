class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}

        nWays = 0
        n = len(nums)

        def explore(index:int, current_sum:int):
            if index == n:
                return 1 if current_sum == target else 0

            if (index, current_sum) in mem:
                return mem[(index, current_sum)]

            value0 = current_sum + nums[index]
            value1 = current_sum - nums[index]    

            w0 = explore(index+1, value0)
            w1 = explore(index+1, value1)

            mem[(index, current_sum)] = w0+w1

            return w0 + w1 
        
        return explore(0, 0)