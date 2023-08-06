# leetcode 57
# Insert newInterval into intervals such that intervals is still sorted 
# in ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary).

# note: [1,2] and [2,3] are considered overlappig in this problem and would need to be merged into [1,3]
# clarify with interviewer what is considered overlapping
# tricky part of this problem is merging multiple overlapping intervals

# merge intervals by taking min of starts and max of ends
# do not add interval to the result until you check to see if intervals overlap

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # create an output array to add intervals to
        output = []

        for i in range(len(intervals)):
            # handle case where newInterval comes before any current interval
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                # at this point we know that every interval that comes next is non overlapping so we can append and return
                return output + intervals[i:] # output array plus the remainder of intervals array

            # handle case where the newInterval goes after the current interval
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
                # we do not return here becuase we could still run in to overlaps
            
            # else, neither of these are true, the interval is for sure overlapping and we need to handle it
            else:
                newInterval = [ min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # let the for loop to continue going through instead of appending here
                # the for loop will handle merging multiple overlaps if they exist using the updated newInterval variable

        output.append(newInterval) # this is for the case that newInterval gets added to the end
        return output

        # O(N) time O(N) space

