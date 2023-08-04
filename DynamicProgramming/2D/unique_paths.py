# leetcode 62

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
# down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# trick to this problem is unique paths from start = (num of possibilities from right cell) + (num of possibilities from dowm cell)
# start from the end (base case is 1 at finish cell) and work our way to the start
#bottom row will always be all ones, rightmost column will always be all ones

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row  = [1]* n # bottom row will always be all ones
        for i in range(m-1): # go through every row except for the bottom one
            newRow = [1] * n
            for j in range(n - 2, -1,-1): #iterate backwards through every column except the rightmost column
                newRow[j] = newRow[j+1] + row[j] # current cell = down cell + right cell
            
            # now update the row array with the newRow
            row = newRow + row
        # return the starting cell's value
        return row[0]
