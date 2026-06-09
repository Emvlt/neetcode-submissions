class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        
        def explore(i, path:List):
            if sum(path) == target:
                self.res.append(path)
                return

            for j in range(i, len(nums)):
                if sum(path) + nums[j] <= target:
                    path.append(nums[j])
                    explore(j, path[:])
                    path.pop(-1)
            return
                    
        self.res = []
        for i in range(len(nums)):
            if nums[i] < target:
                explore(i, [nums[i]])

            elif nums[i] == target:
                self.res.append([nums[i]])

        return self.res