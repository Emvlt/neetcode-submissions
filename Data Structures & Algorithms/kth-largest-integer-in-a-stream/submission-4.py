import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # We begin by making a heap out of nums, in-place
        heapq.heapify(nums)
        # The first element of the heap is the min of nums.
        # We keep poping the heap until it contains the original k largest elements
        while k < len(nums):
            heapq.heappop(nums)

        self.nums = nums
        self.k = k       

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]
        
