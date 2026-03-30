from collections import defaultdict

class Solution:
    def get_signature(self, string:str) -> dict[str, int]:
        signature = defaultdict(int)
        for char in string:
            signature[char]+=1
        return tuple(sorted(signature.items()))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            signature = self.get_signature(string)
            groups[signature].append(string)
        return list(groups.values())
        