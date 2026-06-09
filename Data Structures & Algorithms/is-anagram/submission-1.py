class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bag_s = {chr(97 + i):0 for i in range(26)}
        bag_t = {chr(97 + i):0 for i in range(26)}

        for ss, tt in zip(s,t):
            bag_s[ss] += 1
            bag_t[tt] += 1
        return bag_s == bag_t