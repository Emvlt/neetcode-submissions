class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        cache = [1, 2]

        for i in range(2, n):
            cache.append(cache[i-1] + cache[i-2])

        return cache[-1]




        