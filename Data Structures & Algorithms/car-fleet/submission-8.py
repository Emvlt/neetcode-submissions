import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We begin by creating a sorted lists of (index, position) pairs
        stack = []

        for p in sorted(enumerate(position), key = lambda x:x[1], reverse=True):
            time = (target - p[1]) / speed[p[0]]
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
