# leetcode 73
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# my initial solution was to use extra space to keep track of coordinates where zeroes are
# we can do this without extra space by setting the first value of every row and column containing zero to zero


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        colZero = False # use this flag to determine if the FIRST row needs to be zeroed out

        for r in range(rows):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[r][0] == 0:
                colZero = True
            for c in range(1,columns):
                if matrix[r][c] == 0:
                    # set the first value of the current column to zero to denote the column needs to be zeroed out
                    matrix[0][c] = 0
                    # set the first value of the current row to zero to denote the row needs to be zeroed out
                    matrix[r][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, rows):
            for j in range(1, columns):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(columns):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if colZero:
            for i in range(rows):
                matrix[i][0] = 0

#o(m*n) time, o(1) space