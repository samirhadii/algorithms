#leetcode 300
#Given an integer array nums, return the length of the longest strictly increasing subsequence

#use a bottom-up approach and start from the last index to work backwards
#base case is that the last index longest subsequence is itself, 1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]* len(nums)

        for i in range(len(nums)-1,-1,-1): # iterate backwards
            for j in range(i+1,len(nums)): # iterate forward from current index
                if nums[i] < nums[j]: # check to see if its increasing
                    dp[i] = max(dp[i], 1+ dp[j])
        
        return max(dp)

# o(n^2) solution