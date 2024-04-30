class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0

        def count(i, j, res):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == '1':
                grid[i][j] = res
                count(i - 1, j, res)
                count(i + 1, j, res)
                count(i, j - 1, res)
                count(i, j + 1, res)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    count(i, j, res)
        return res