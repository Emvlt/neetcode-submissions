class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        solutions = []

        def backtracking(index:int, sol:List):
            # Stop 
            if sum(sol) == target:
                solutions.append(sol[:])
                return

            if sum(sol) > target:
                return

            for j in range(index, n):
                sol.append(nums[j])
                backtracking(j, sol)
                sol.pop()


        backtracking(0, [])
        return solutions