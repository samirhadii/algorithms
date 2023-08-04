#Given an integer array nums representing the amount of money of each house
#return the maximum amount of money you can rob tonight
#the houses are arranged in a circle (first house in list is adjacent to last house in list)
#you cannot rob adjacent houses

class Solution:
    def rob(self, nums: List[int]) -> int:
        #dynamic programming optimized tabulization approach same as house robber 1
        #only difference is that we will compute the the maxes for starting at index 0 and index 1 seperately

        #handle edge cases
        if nums is None or len(nums) ==0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.house_rob_helper(nums[:-1]),    #starting at index 0,we will not include the last index
        self.house_rob_helper(nums[1:]))                #starting at index 1 we are allowed to go to the end of the array

        #helper function that uses the same logic from house robber 1
    def house_rob_helper(self,houses): #helper function takes in the int array of houses and their values
        rob_nonadjacent = 0 #the house before the house we just robbed
        rob_adjacent = 0 #the house we just robbed
        for current_house in houses:
            temp = max(current_house + rob_nonadjacent, rob_adjacent) #max we can rob up until the current
            rob_nonadjacent = rob_adjacent
            rob_adjacent = temp

        return rob_adjacent #at the end of the iteration this will be the last value we computed and will store the final max

