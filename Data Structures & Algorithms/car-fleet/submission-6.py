import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We begin by creating a sorted lists of (index, position) pairs
        index_pos_pairs = sorted(enumerate(position), key = lambda x:x[1], reverse=True)

        stack = []

        for p in index_pos_pairs:
            time = (target - position[p[0]]) / speed[p[0]]
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
