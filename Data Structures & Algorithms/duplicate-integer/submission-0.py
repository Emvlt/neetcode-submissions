class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()

        for n in nums:
            if n in vals:
                return True

            vals.add(n)

        return False
        