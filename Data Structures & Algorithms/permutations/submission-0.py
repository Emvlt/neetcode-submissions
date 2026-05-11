class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        n = len(nums)

        used = [False for i in range(n)]

        def backtracking(i, sol):
            if len(sol) == n:
                solutions.append(sol[:])

            for j in range(n):
                if not used[j]:
                    sol.append(nums[j])
                    used[j] = True
                    backtracking(j+1, sol)
                    sol.pop()
                    used[j] = False
                               
        backtracking(0, [])
        return solutions