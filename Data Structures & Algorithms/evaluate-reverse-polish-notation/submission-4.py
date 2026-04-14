class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def isOperator(token: str):
            return token in ['*', '+', '-', '/']

        def action(operator:str, v0:int, v1:int):
            if operator == '*':
                return v0*v1
            elif operator == '/':
                if v1 == 0:
                    return 0
                return int(v0/v1)

            elif operator == '+':
                return v0+v1

            elif operator == '-':
                return v0-v1

            else:
                raise ValueError

        stack = []

        for token in tokens:
            if isOperator(token):
                v1 = stack.pop()
                v0 = stack.pop()
                stack.append(action(token, v0, v1))

            else: 
                stack.append(int(token))

            print(stack)

        return stack[-1]
        