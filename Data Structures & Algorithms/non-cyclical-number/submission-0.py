class Solution:
    def isHappy(self, n: int) -> bool:

        def getSumSquareDigits(n: int) -> int:
            string = str(n)
            res = 0
            for char in string:
                res += int(char)**2
            return res     

        number_set = set()

        while True:
            n = getSumSquareDigits(n)
            if n == 1:
                return True
            
            if n in number_set:
                return False

            number_set.add(n)
        