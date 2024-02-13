# leetcode 130
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Modify the board in place

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start at the borders of the grid because that is the only possible point for an unsurrounded region
        # then run dfs on any O's you see on the border and change them to "#"
        # change the # to O's at the end of the program and turn everything else into X's

        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):
            if (r < 0) or (c < 0) or (r >= rows) or (c >= cols) or (board[r][c] != "O"):
                return
            board[r][c] = "#"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # iterate through the borders of the grid and run dfs if we find an "O"

        for top_ind in range(cols):
            if board[0][top_ind] == "O":
                dfs(0,top_ind)
        for right_ind in range(1,rows): # disregard top right row bc we already visited 
            if board[right_ind][cols-1] == "O":
                dfs(right_ind,cols-1)
        for bottom_ind in range(cols -1): #disregard bottom right
            if board[rows-1][bottom_ind] == "O":
                dfs(rows-1,bottom_ind)
        for left_ind in range(1,rows-1): #ignore top left and bottom left
            if board[left_ind][0] == "O":
                dfs(left_ind,0)
        
        # now that the entire board is marked, iterate through every place
        # mark O's -> X's and mark #'s -> O's

        for r in range(rows):
            for c in range(cols):
                if board[r][c] =="O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"





        