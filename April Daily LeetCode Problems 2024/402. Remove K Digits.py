class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k > 0 , remove rmaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack

        result = ''.join(stack).lstrip('0')

        return result if result else '0'
