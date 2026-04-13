class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maximum = 1
        nums = set(nums)

        for n in nums:
            # is n the start of a sequence?
            if n-1 not in nums:
                i = 1
                current_max = 1
                while n+i in nums:
                    current_max += 1
                    i += 1
                if current_max > maximum:
                    maximum = current_max

        return maximum