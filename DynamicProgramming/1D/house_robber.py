#leetcode 198, medium
#You are a professional robber planning to rob houses along a street. 
#cannot rob two adjacent houses
#Given an integer array nums representing the amount of money of each house,
#return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom-up tabulization approach
        #only store the previous two results because we update the max possible at every step

        #handle empty array case
        if not nums:
            return 0

        rob_nonadjacent = 0 #the house before the house we just robbed
        rob_adjacent = 0 #the house we just robbed
        for current_house in nums:
            temp = max(current_house + rob_nonadjacent, rob_adjacent) #max we can rob up until the current
            rob_nonadjacent = rob_adjacent
            rob_adjacent = temp

        return rob_adjacent #at the end of the iteration this will be the last value we computed and will store the final max

#time complexity O(N) 
#space complexity O(1)      