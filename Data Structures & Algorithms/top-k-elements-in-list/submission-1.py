from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counting the frequency of each numbers
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        # Putting the number occuring at a given frequency in the appropriate bucket 
        frequencies = [[] for i in range(len(nums)+1)]
        for key, value in hashmap.items():
            frequencies[value].append(key)

        result = []
        for freq in reversed(frequencies):
            for num in freq:
                result.append(num)
                if len(result) == k:
                    return result

        
        