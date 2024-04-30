class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n = len(land)
        m = len(land[0])
        result = []
        visited = [[False] * m for _ in range(n)]
        for r1, c1 in product(range(n), range(m)):
            if land[r1][c1] == 0 or visited[r1][c1]:
                continue
            r2, c2 = r1, c1
            while True:
                visited[r2][c2] = Tru
                ''
                if r2 + 1 < n and land[r2 + 1][c2] == 1:
                    r2 += 1
                elif c2 + 1 < m and land[r1][c2 + 1] == 1:
                    r2 = r1
                    c2 += 1
                else:
                    break
            result.append([r1, c1, r2, c2])

        return result

