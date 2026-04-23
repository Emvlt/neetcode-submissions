class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        self.solutions = []

        def partition(s:str, substrings):
            if not s:
                self.solutions.append(substrings[:])
                return
            for i in range(1, len(s)+1):
                prefix = s[:i]
                suffix = s[i:]
                if isPalindrome(prefix):
                    substrings.append(prefix)
                    partition(suffix, substrings)
                    substrings.pop()

        partition(s, [])
        return self.solutions