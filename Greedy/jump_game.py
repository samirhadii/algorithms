# leetcode 55 

# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# we can iterate backwards through every value and if the value is >= target we set target to current index
# once we exit the reverse for loop, if the target is not at index zero, it is impossible to reach.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        #initialze target as the last number in array
        target = nums[len(nums)-1]
        #work backwards through the array
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= target: # this means that you can reach the target
                target = i # set target to the current index
        
        return target == 0 
        # if target is at the zero index, this means that it is possible to jump and we return true
        # O(n) time complexity, O(1) space