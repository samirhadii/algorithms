# leetcode 53 
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# keep a local max and a final max
# since we are only returning the sum, we only need to iterate through every number and return the final max sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize final and local max with the first value
        final_max = nums[0]
        local_max = nums[0]

        for num in nums[1:]: # iterate thtrough the rest of the numbers in the list
            local_max = max(num, num + local_max)
            #update final max if local max has now become greater
            if local_max > final_max:
                final_max = local_max
        #after iteration is done, final_max will have the answer stored
        return final_max
    