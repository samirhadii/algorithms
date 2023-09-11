# leetcode 1293
# Shortest Path in a Grid with Obstacles Elimination
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
# You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) 
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. 
# If it is not possible to find such walk return -1.

# usually for a shortest path, you use breadth first search algorithm.
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        target = (rows-1, cols-1) # store target as an x,y tuple

        # return manhattan distance if we are allowed to eliminate all possible obstacles
        if k >= rows + cols -2:
            return rows + cols -2
        
        # current state will store row, column and remaining obstacle eliminations
        state = (0, 0, k)
        # queue holds current number of steps, and state
        q = deque([(0, state)])
        # visited set to store visited nodes
        visit = set([state])

        while q:
            steps, (row, col, k) = q.popleft()

            if (row, col) == target: # base case, reach target return current steps (will be shortest number of steps)
                return steps
            
            # now explore all four directions 
            four_directions = [(row,col + 1),(row + 1,col),(row,col - 1),(row - 1,col)]
            for new_r, new_c in four_directions:
                # check if (new_r, new_c) is in bounds
                if (0<= new_r < rows) and (0 <= new_c < cols):
                    new_elims = k - grid[new_r][new_c]
                    new_state = (new_r, new_c, new_elims)
                    # if we still have available eliminations, move to next value in the queue
                    if new_elims >= 0 and new_state not in visit:
                        visit.add(new_state)
                        q.append((steps + 1, new_state))


        # if target is never reached
        return -1
        