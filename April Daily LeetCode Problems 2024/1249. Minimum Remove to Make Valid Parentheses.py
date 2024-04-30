class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        s = list(s)
        stack = []

        for i in range(len(s)):

            if s[i] == '(':

                stack.append(i)

            elif s[i] == ')':

                if len(stack) > 0:

                    stack.pop()

                else:

                    s[i] = ''

        while len(stack) > 0:
            s[stack[-1]] = ''

            stack.pop()

        return ''.join(s)