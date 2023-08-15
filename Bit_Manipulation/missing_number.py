# leetcode 268
# Given an array nums containing n distinct numbers in the range [0, n]
# return the only number in the range that is missing from the array.


# use xor operator to solve this 
# we do (3 ^ 3) we will get zero 
# the order we xor numbers does not matter because once we get a zero, the xor operation will return the non zero numbers
# example (5 ^ 5 ^ 3) the (5^5) will return zero and the (0^3) will return 3 because its binary representation is 011 xor 000 will return 011
# to solve this problem we will loop through to length n, xor with every value in nums, and the missing number will be left
class Xor_Solution:
    def xorMissingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# solution using gauss' formula to find the expected sum of all numbers to n 
# and subtract from actual sum of the array to find the missing number
class Gauss_Solution:
    def gaussMissingNumber(self, nums: List[int]) -> int:
        # take the expected sum, 0 -> n  and subtract from actual sum to get missing number
        # use gauss' formula to find expected sum quicker than looping through length
        expected_sum = (len(nums) * (len(nums)+1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
