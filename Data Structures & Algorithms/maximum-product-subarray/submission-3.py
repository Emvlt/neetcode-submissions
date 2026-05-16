class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mini = 1
        maxi = 1
        for el in nums:
            temp = maxi * el   
            maxi = max(el, maxi*el, mini*el)
            mini = min(el, temp, mini*el)
            res = max(res, maxi)
            
        return res