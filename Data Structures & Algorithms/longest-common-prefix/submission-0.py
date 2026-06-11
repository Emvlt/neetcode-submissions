class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        m = min([len(s) for s in strs])

        for char_index in range(m):
            c = strs[0][char_index]

            if all(strs[str_index][char_index] == c for str_index in range(1, len(strs))):
                res += c

            else:
                break

        return res