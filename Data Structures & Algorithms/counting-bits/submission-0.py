class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(string:str) -> int:
            count = 0
            for c in string:
                if c == '1':
                    count += 1
            return count

        L = []
        for i in range(n+1):
            bin_repr = bin(i)
            L.append(countOnes(bin_repr[2:]))
        return L
        