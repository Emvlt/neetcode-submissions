class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myset = set()
        for n in nums:
            if n in myset:
                myset.remove(n)
            else:
                myset.add(n)
        return myset.pop()