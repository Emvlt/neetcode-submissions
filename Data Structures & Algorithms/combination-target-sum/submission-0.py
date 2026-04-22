class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solutions = []
        nums.sort()  # Sorting allows us to stop early if the number is too big

        def explore(index: int, current_sum: int, els: List[int]):
            # Base Case 1: We found a valid combination
            if current_sum == target:
                # We append a COPY of els using els[:] or list(els)
                self.solutions.append(els[:])
                return

            # Base Case 2: We exceeded the target, no need to continue
            if current_sum > target:
                return

            # Explore horizontally: try each number starting from 'index'
            # We use 'index' to avoid duplicate combinations like [2, 3] and [3, 2]
            for i in range(index, len(nums)):
                # CHOOSE: Add the current number
                els.append(nums[i])
                
                # EXPLORE: Recurse! 
                # Note: We pass 'i' as the next index because we can reuse the same number
                explore(i, current_sum + nums[i], els)
                
                # UN-CHOOSE: This is the backtracking step. 
                # We remove the last number so the loop can try the next 'nums[i]' 
                # with the original list state.
                els.pop()

        # Kick off the recursion starting at the first index with an empty sum/list
        explore(0, 0, [])
        return self.solutions