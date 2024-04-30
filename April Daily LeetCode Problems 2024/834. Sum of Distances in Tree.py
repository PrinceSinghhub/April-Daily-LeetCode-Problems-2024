class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)

        size = [0] * n

        def fn(x, par):
            """Return size and sum of distances in sub-tree."""
            c = s = 0
            for xx in graph.get(x, []):
                if xx != par:
                    cc, ss = fn(xx, x)
                    c, s = c + cc, s + ss + cc
            size[x] = c + 1
            return c + 1, s

        ans = [0] * n
        ans[0] = fn(0, -1)[1]

        stack = [0]
        while stack:
            x = stack.pop()
            for xx in graph.get(x, []):
                if not ans[xx]:
                    ans[xx] = ans[x] + n - 2 * size[xx]
                    stack.append(xx)
        return ans