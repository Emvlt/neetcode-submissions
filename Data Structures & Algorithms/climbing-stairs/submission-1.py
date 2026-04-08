class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        cache = [0 for i in range(n)]
        cache[0] = 1
        cache[1] = 2

        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[-1]




        