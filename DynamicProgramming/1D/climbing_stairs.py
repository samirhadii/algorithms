#leetcode 70, easy
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        #true dyanmic programming approach
        #approach: use the next two values to calculate the current value because every subproblem depends on the last subproblem
        #since we only depend on two values at a time we don't need an entire memoization table
        #we will only store the two next values as variables and reassign their values

        one_step = 1 #stored value to denote how many distinct ways if you choose one step per turn, base case set to one
        two_steps = 1 #stored value to denote how many distinct ways if you choose two steps per turn, base case set to one

        for i in range(n-1): #loops through n-1 times and returns the one_step value at the end
            temp = one_step #store one value to reassign it to two_steps after one is updated
            one_step = one_step + two_steps
            two_steps = temp
        #wherever the one_step value lands after n-1 times, we return it.
        return one_step
    #O(N)time complexity and O(1) space complexity