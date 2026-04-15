class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        nums.sort()

        for i, value in enumerate(nums[:-2]):
            if value > 0:
                break
            if i > 0 and nums[i-1] == value:
                continue

            target = -value
            j = i + 1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    solutions.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
        return solutions

            

        