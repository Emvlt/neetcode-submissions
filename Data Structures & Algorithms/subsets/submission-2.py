class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        solutions  = []
        n = len(nums)

        def backtracking(index:int, sol : List) -> List:
            solutions.append(sol[:])
            for j in range(index, n):

                sol.append(nums[j])

                backtracking(j+1, sol)

                sol.pop()

        backtracking(0, [])
        return solutions