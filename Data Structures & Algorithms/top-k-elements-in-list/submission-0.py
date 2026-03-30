from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num]+=1

        d = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        return list(d.keys())[:k]