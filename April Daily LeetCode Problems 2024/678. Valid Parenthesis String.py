class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                star_stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while stack and star_stack:
            if stack[-1] > star_stack[-1]:
                return False
            stack.pop()
            star_stack.pop()

        return not stack