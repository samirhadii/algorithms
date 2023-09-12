# leetcode 1730
# shortest path to get food

# You are given an m x n character matrix, grid, of these different types of cells:

# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # use a list to represent a queue data structure
        q = []
        # visited set
        visit = set()

        rows = len(grid)
        cols = len(grid[0])
        start = (-1,-1)

        # find the location of * and perform bfs on int
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    start = (r,c,0)
                    q.append(start) # add start val and current distance to queue
                    visit.add((r,c))
                    break
        

        while q:
            cur_r, cur_c, cur_dis = q.pop(0)
            if grid[cur_r][cur_c] == "#": # if found, retun current distance
                return cur_dis
            neighbors = [[cur_r + 1, cur_c],[cur_r, cur_c + 1],[cur_r - 1, cur_c],[cur_r, cur_c -1]]
            for nr, nc in neighbors:
                # check validity
                if (0<= nr < rows) and (0<= nc < cols) and ((nr,nc) not in visit) and(grid[nr][nc] != "X"):
                    visit.add((nr,nc))
                    coords = (nr,nc,cur_dis + 1) 
                    q.append(coords)
        
        # if the target is never found, return -1
        return -1

# time complexity O(r * c) r = num of rows, c = num of columns. Worst case we will visit every element once.
# space complexity: O(r * c)
