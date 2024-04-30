class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ans = 0
        s = s.strip()
        for val in s[::-1]:
            if val == " ":
                break
            else:
                ans += 1

        return ans
