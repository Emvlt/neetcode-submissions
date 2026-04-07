class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        def matches(c1, c2) -> bool:
            return (c1=='{' and c2=='}') or (c1=='(' and c2==')') or (c1=='[' and c2==']')

        def isOpen(c : str) -> bool:
            return True if c in ['{', '[', '('] else False

        stack = []

        for i in range(len(s)):
            c = s[i]
            if isOpen(c):
                stack.append(c)
            else:
                if not stack:
                    return False
                if not matches(stack[-1], c):
                    return False
                stack.pop(-1)

        return not stack
