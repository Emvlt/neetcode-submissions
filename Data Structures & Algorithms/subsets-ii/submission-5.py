class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        n = len(nums)

        nums.sort()

        def backtracking(i, sol:List):
            solutions.append(sol[:])

            for j in range(i, n):
                if j>0 and i!=j and nums[j]==nums[j-1]:
                   continue
                else:
                    sol.append(nums[j])
                    backtracking(j+1, sol)
                    sol.pop()



        backtracking(0, [])
        return solutions