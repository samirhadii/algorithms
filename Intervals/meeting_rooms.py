# leetcode 252
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# sort the intervals and compare end times to next start times

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort by start index and if any intervals overlap, return false
        intervals.sort(key = lambda i : i[0])

        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True


# o(nlogn) time complexity

