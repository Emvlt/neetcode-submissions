class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        solutions = []

        # Inplace sorting of the small list
        candidates.sort()

        def backtracking(i, sol):
            if sum(sol) > target:
                return

            if sum(sol) == target:
                solutions.append(sol[:])
                return

            for j in range(i, n):
                if j > 0 and j>i and candidates[j] == candidates[j-1]:
                    continue
                else:
                    sol.append(candidates[j])
                    backtracking(j+1, sol)
                    sol.pop()

        backtracking(0, [])
        return solutions