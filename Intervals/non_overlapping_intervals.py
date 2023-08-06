# leetcode 435
# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# make sure to clarify with interviewer what is considered overlapping!
# in this problem, intervals = [[1,2],[2,3]] are considered non-overlapping

# reminder: we are only returning the minimum NUMBER we need to remove, not the actual interval needed to be removed.

# solve by sorting the intervals by the starting point and compare adjacent intervals
# when finding an adjacent interval you want to keep the interval that ends first!

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the intervals O(nlogn)
        intervals.sort()

        output = 0
        # keep track of previous intervals endpoint in order to find overlaps
        prevEnd = intervals[0][1] # initialize as first intervals endpoint

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # not overlapping, update prevEnd
                prevEnd = end
            else:
                output += 1
                # don't actually have to delete the overlap in this problem
                # we would keep the intereval that ends first, so update prevEnd accordingly
                prevEnd = min(prevEnd,end)

        return output

# time o(nlogn), space o(1)
