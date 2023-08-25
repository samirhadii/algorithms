# leetecode 371
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# one looks like this in binary: 01
# two looks like this in binary: 10
# adding the two would be: 11

# if either digit is a one, the output is a one
# if BOTH digits are a one, the output is a zero, and we need to carry the one to remaining digits
# if both digits are zero, the output is zero
# this is similar to the xor operator, but still need to figure out how to carry the 1 for the 1 + 1 case

# use the and operator to get all of the remainders. 1 & 1 = 1 
# shift the result of the and operation to the left by one in order to deal with the carry

# once the and operation between a and b returns zero, that means there are no more remainder carrys
# keep looping through and doing the xor + and operations until the and operation returns zero

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign




