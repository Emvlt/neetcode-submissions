class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hashmap = {0:0}

        def BFS(target):
            if target in hashmap:
                return hashmap[target]

            leaves = []
            for c in coins:
                if c <= target:
                    res = BFS(target-c)
                    if res != -1:
                        leaves.append(res)

            if leaves:
                hashmap[target] = 1+ min(leaves)
            else:
                hashmap[target] = -1

            return hashmap[target]

        return BFS(amount)
        

        