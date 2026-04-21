class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])

        def inbound(r, c):
            return 0<=r<n and 0<=c<m

        def dfs(r, c, visited):
            if not inbound(r, c):
                return 1 
            if grid[r][c]==0:
                return 1 
            if (r, c) in visited:
                return 0
            
            visited.add((r,c))
            ans = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                ans += dfs(nr, nc, visited)
            return ans
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return dfs(r, c, set())        