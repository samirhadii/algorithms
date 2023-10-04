# leetcode 694
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) 
# to equal the other.
# Return the number of distinct islands.

# finding the nighbors can be done with either bfs or dfs solution
# hard part of this is distinguishing between distinct islands
# finding unique islands can be done by storing coordinates of each island from a relative start point
# the relative point should be (0,0) and can be stored this way by subtracting every coordinate in the island by the topleftmost coordinate

# avoid the need to worry about order of coordinates by ensuring that two islands are initially discovered from the same relative cell. 
# This can be done by iterating left to right up to down

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        rows = len(grid)
        cols = len(grid[0])
        # dfs function to check for island
        def dfs(r,c,island_coords,start_value):
            if (r < 0) or (r >= rows) or (c < 0) or (c >= cols) or grid[r][c] != 1:
                return
            # add coordinates to current island coordinate list
            # make coordinates relative
            island_coords.append((r-start_value[0],c-start_value[1]))
            # set the value of the current land to # 
            grid[r][c] = 0
            # run depth first search on all possible neighbors of (r,c)
            dfs(r+1,c,island_coords,start_value)
            dfs(r-1,c,island_coords,start_value)
            dfs(r,c+1,island_coords,start_value)
            dfs(r,c-1,island_coords,start_value)
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_coords = []
                    start_value = (r,c)
                    dfs(r,c,island_coords,start_value)
                    islands.add(tuple(island_coords))
        return len(islands)