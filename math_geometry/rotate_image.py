# leetcode 48 
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# must rotate the image in-place

# create boundries, left and right boundries, top and bottom boundries
# move boundries every time you need to go into an inner layer

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1 #since length and width are the same in this problem, this is ok
        while l<r:
            for i in range(r-l):
                top = l
                bottom = r
                #save topleft value into temp var
                topLeft = matrix[top][l+i]
                #move bottom left into topleft
                matrix[top][l+i] = matrix[bottom-i][l]
                #move bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                #move top left to top right
                matrix[top+i][r] = topLeft
            r-=1
            l+=1
            