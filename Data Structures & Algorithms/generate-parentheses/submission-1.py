class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []

        def explore(s:str, n_open = 0, n_closed = 0):
            if len(s) == 2*n:
                solutions.append(s)
                return 
            if n_open < n:
                explore(s + "(", n_open+1, n_closed)

            if n_closed < n_open:
                explore(s + ")", n_open, n_closed+1)

        explore("", 0, 0)
        return solutions