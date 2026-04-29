from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = tuple(wordDict)        

        @lru_cache
        def can_construct(current_s):
            if not current_s:
                return True

            for w in wordDict:
                if current_s.startswith(w):
                    suffix = current_s[len(w):]
                    if can_construct(suffix):
                        return True

            return False
            
        return can_construct(s)