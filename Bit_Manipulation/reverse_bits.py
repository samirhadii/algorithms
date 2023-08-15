# leetcode 190
# Reverse bits of a given 32 bits unsigned integer.

# iterate trhough every bit using the shift >> operator
# iterating through every single bit of the 32 bit integer, we can get the current bit's value by using the & 1 operation (logic and)
# 0 & 1 = 0 , 1 & 1 = 1 

# reverse the bits by adding the current bit to 31 - the current place in the output 
# use logic or (|) when reassigning values to the output becuase we will default have 0 there
# 0 | 1 = 1 , 0 | 0 = 0
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # all 32 bits are initialized as zero
        for i in range(32): # go through every single bit up to 32
            # get the ith bit of n by shifting to the right
            bit = (n>>i) & 1 # bit will either be 1 or 0 
            # use logic or to add bit to the output
            # update in reverse order using bit shift in order using i
            res = res | (bit << (31-i))
        return res

# o(32) constant time
# solution will never scale with a different input so it is o(32) constant


