# leetcode 338
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

# use the most significant bit to cut down on repeated work of having to calculate hamming weight for each index
# most significant bits are powers of 2 you can check this by multiplying prev significant bit by 2
# this is a dynamic programming solution that cuts out repeat work

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        current_significant = 1

        for i in range(1, n + 1):
            if current_significant * 2 == i:
                current_significant = i
            dp[i] = 1 + dp[i - current_significant]
        
        return dp

#o(n) time, o(n) space

