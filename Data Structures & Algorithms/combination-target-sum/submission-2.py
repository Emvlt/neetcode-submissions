class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solutions = []
        nums.sort()  # Sorting allows us to stop early if the number is too big

        def explore(sol: List[int], index: int, current_sum: int):
            if current_sum == target:
                self.solutions.append(sol[:])
                return
            
            elif current_sum > target:
                return 

            for i in range(index, len(nums)):
                sol.append(nums[i])
                explore(sol, i, current_sum + nums[i])
                sol.pop()

        
        explore([], 0, 0)
        return self.solutions