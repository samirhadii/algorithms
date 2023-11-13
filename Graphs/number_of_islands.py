# leetcode 200
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        totalIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # check in bounds
            if (r < 0) or (c < 0) or (r >= rows) or (c >= cols) or (grid[r][c] != "1"):
                return
            else:
                # mark as visited
                grid[r][c] = "0"
                # run dfs on all neighbors
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(
                        r, c
                    )  # will run through every adjacent '1' and add it to visited
                    totalIslands += (
                        1  # increment totalIslands since we haven't visited this 1 yet
                    )

        return totalIslands



sol = Solution()
test_grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(test_grid))