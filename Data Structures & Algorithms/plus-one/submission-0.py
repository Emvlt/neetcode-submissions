class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        i = 0
        for d in digits[::-1]:
            res += d * 10**i
            i += 1

        res += 1

        return [int(c) for c in str(res)]
        