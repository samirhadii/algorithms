# leetcode 1143

# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# visualize text1 and text2 as the x and y axis of a 2D array.
# initialize the bottom row and the right column of the 2D array as all zeroes 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize a 2D array len(text2) +1 x len(text1)+1 with zeroes
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] 

        print(dp) # figure out which side is which x or y axis

        # iterate through the 2D grid in reverse order
        for i in range(len(text1) - 1, -1 , -1):
            for j in range(len(text2) - 1, -1 , -1):
                if text1[i] == text2[j]:
                    # if chars match, perform one plus diagonal value
                    dp[i][j] = 1 + dp[i + 1][j + 1] # one plus i & one + j to get diagonal
                else:
                    # else chars don't match fill in the longest possible subseq at this point
                    dp[i][j] = max(dp[i][j + 1] , dp[i + 1][j])
                
        #after the entire dp matrix is filled in, the result is at the top of the matrix
        return dp[0][0]

        # time complexity O(n * m), space complexity O(n * m)