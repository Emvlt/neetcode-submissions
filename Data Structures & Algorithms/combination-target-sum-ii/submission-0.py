class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.solutions = []

        def explore(index, current_sum, elements):
            if current_sum == target:
                self.solutions.append(elements[:])
                return 

            elif current_sum > target:
                return

            for j in range(index, len(candidates)):
                if candidates[j] == candidates[j-1] and index < j:
                    pass
                else:
                    elements.append(candidates[j])
                    explore(j+1, current_sum + candidates[j], elements)
                    elements.pop()

        explore(index = 0, current_sum = 0, elements = [])
        return self.solutions