#leetcode 322
# You are given an integer array coins representing coins of 
# different denominations and an integer amount representing 
# a total amount of money.

# Return the fewest number of coins that you need to make up 
# that amount. If none, return -1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #take a bottom-up dynamic programming approach
        #go from zero to the target amount, and fill in the minimum amount of coins it takes to get to the target amount
        dp = [amount+1] * (amount+1) #array should go from zero to amount +1. Initialize it as amount+1 so we can reset it with the minimum amount later
        #set the first value to zero
        dp[0] = 0

        #fill out the dp array from the bottom up. 1 to the amount
        for a in range(1,amount+1):
            #goes through every coin 
            for c in coins:
                if a-c >=0: #if current is non-negative we can keep searching
                    dp[a] = min(dp[a], 1 + dp[a-c]) #one is the current coin, a-c is the amount in dp we are searching for
    
        #return the amount stored at the final slot if the amount is NOT the default value we set previously
        #else that means we could not find a possible combination so return -1
        return dp[amount] if dp[amount] != amount+1 else -1
#time complexity O(the amount given * the number of coins given)
#space complexity O(amount given)