# leetcode 191
# Write a function that takes the binary representation of an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).

# solve this by using the mod operator. if a value %2 == 1 then this value is a one
# we can iterate thtrough each bit by using the bit shift operator
# bit shift to the right >>

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            # if n%2 == 1, the integer is one and we add it, otherwise will be zero 
            count += (n%2)
            n = n >> 1 # shift bits one to the right

        return count
    
    # time complexity will be o(32) because we know it will always be a 32 bit input