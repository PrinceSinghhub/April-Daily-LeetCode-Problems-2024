MOD = 1_000_000_007


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ans = 0
        n = len(ring)
        ring = ring + ring + ring
        closestl = [[] for j in range(n)]
        closestr = [[] for j in range(n)]
        curr = [-1 for i in range(26)]
        for i in range(2 * n):
            curr[ord(ring[i]) - 97] = i % n
            if i >= n:
                closestl[i % n] = list(curr)
        curr = [-1 for i in range(26)]
        for i in range(3 * n - 1, n - 1, -1):
            curr[ord(ring[i]) - 97] = i % n
            if i < 2 * n:
                closestr[i % n] = list(curr)
        memo = {}

        def solve(curr, pos):
            strpath = str(curr) + ',' + str(pos)
            if strpath in memo:
                return memo[strpath]
            if curr >= len(key):
                return 0

            memo[strpath] = MOD
            l = closestl[pos][ord(key[curr]) - 97]
            r = closestr[pos][ord(key[curr]) - 97]
            if l <= pos:
                memo[strpath] = min(memo[strpath], 1 + pos - l + solve(curr + 1, l))
            else:
                memo[strpath] = min(memo[strpath], 1 + (pos + n - l) + solve(curr + 1, l))

            if r >= pos:
                memo[strpath] = min(memo[strpath], 1 + r - pos + solve(curr + 1, r))
            else:
                memo[strpath] = min(memo[strpath], 1 + (r + n - pos) + solve(curr + 1, r))
            return memo[strpath]

        return solve(0, 0)


