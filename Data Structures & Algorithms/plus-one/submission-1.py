class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        r = 1
        for d in digits[::-1]:
            if r+d == 10:
                res.insert(0, 0)
            else: 
                res.insert(0, d+r)
                r = 0 
        if r==1:
            res.insert(0, 1)
        return res

        