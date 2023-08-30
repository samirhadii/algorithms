# leetcode 1356
# JPMorgan, goldman, accenture flagged question
# You are given an integer array arr. Sort the integers in the array in ascending order by 
# the number of 1's in their binary representation and in case of two or more integers have the 
# same number of 1's you have to sort them in ascending order.

# instead of using the bin() function, let's use bitwise functions
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # helper function to count 1's
        def count_ones(n):
            count = 0
            while n:
                count += n & 1 # if the current last bit is one, count will increment by 1
                n >>= 1 # right shift to use the next bit
            return count
        
        counted_arr = []
        for num in arr:
            counted_arr.append((num,count_ones(num))) #create a list of tuples, (number, count of ones). Tuple is slight optimization over lists
        # sort by the second element in each tuple x[1], then if elements are the same sort by first element x[0]
        counted_arr.sort(key=lambda x: (x[1],x[0]))
        # result should be just the original numbers
        result = [num[0] for num in counted_arr]
        return result