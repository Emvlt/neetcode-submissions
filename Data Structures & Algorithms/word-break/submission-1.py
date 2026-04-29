from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # We break down the List of strings into a hashable object (tuple)
        wordDict = tuple(wordDict)

        # We define a helper function that tells us is a string can be constructed
        # We use lru_cache to cache the substrings already checked
        @lru_cache
        def can_construct(substring) -> bool:
            # Base condition
            if not substring:
                return True

            for word in wordDict:
                if substring.startswith(word):
                    suffix = substring[len(word):]
                    if can_construct(suffix):
                        return True

            # Fallback
            return False

        return can_construct(s)