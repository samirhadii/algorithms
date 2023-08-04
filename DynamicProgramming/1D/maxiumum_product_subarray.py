#leetcode number 152
#Given an integer array nums, find a subarray that has the largest product, and return the product.

#cases that need to be handled are zeroes and negative numbers
#zeroes will reset the current combo which should be stored in res if its the new max combo
#negatives will suddenly turn a large number into a minimum number but can be reversed again into a large number by encountering another negative

#with this in mind, we will iterate through every number and update the maxes and mins as outlined
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        res = max(nums) #initialize as largest element in array, if no combo is greater we will simply return the max
        #initialize the currents as 1 so we can easily perform multiplication on the first step
        current_min =1
        current_max =1

        for n in nums:
            tmp = current_max*n
            current_max = max(n*current_max, n*current_min, n)
            current_min = min(tmp,n*current_min,n)
            res = max(res,current_max)

        return res
