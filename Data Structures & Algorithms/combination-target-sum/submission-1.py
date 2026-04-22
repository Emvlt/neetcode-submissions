class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solutions = []
        nums.sort()  # Sorting allows us to stop early if the number is too big

        def explore(index: int, current_sum: int, els: List[int]):
            if current_sum == target:
                self.solutions.append(els[:])
                return 
            elif current_sum > target:
                return

            for i in range(index, len(nums)):
                els.append(nums[i])

                explore(i, nums[i] + current_sum, els)

                els.pop()

        # Kick off the recursion starting at the first index with an empty sum/list
        explore(0, 0, [])
        return self.solutions