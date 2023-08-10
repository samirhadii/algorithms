# leetcode 54 
# Given an m x n matrix, return all elements of the matrix in spiral order.

# create boundries for the matrix you're in
# iterate through the layers of the matrix: topmost row, rightmost column, bottommost row, leftmost column
# after each iteration decrement the boundry pointer

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # initialize boundry pointers
        left =0
        right = len(matrix[0])
        top=0
        bottom = len(matrix)
        
        while left < right and top < bottom:
            # iterate through topmost row (left to right)
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            # iterate through the rightmost column (top to bottom)
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1

            # check to ensure that the pointers have not crossed
            # this will take care of single row or single column matrixes
            if not (left<right and top<bottom):
                break
            
            # iterate through the bottom row (right to left)
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            # iterate through leftmost row (bottom to top)
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        # return fully populated result array 
        return res