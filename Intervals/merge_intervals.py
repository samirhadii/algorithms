# leetcode 56
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# trick is to sort every subarray by the first element
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the first element in each subarray ascending order O(nlogn) operation
        intervals.sort(key = lambda i : i[0])
        # initialize output array with first value
        output = [intervals[0]]
        
        # iterate through the array and merge overlaps
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])

        return output