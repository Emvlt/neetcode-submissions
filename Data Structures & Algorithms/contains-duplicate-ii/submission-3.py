class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        table = set()

        # initialisation
        for i in range(k+1):
            if i >= len(nums):
                return False
            if nums[i] in table:
                return True
            table.add(nums[i])

        for i in range(k+1, len(nums)):
            table.remove(nums[i-(k+1)])
            if nums[i] in table:
                return True
            table.add(nums[i])

        return False

         