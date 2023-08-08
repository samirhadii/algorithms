# leetcode 253
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

# when two meetings overlap with each other, you need another meeting room

# keep track of the current amount of meetings going on at any time then return the max of that number
# keep track of meetings by making two seperate arrays, one for start times and one for end times

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        meeting_rooms = 0
        result = 0
        # create array for all start times
        start_array = sorted([i[0] for i in intervals])
        end_array = sorted([i[1] for i in intervals])

        start_pointer = 0
        end_pointer = 0

        # if a current start time is less than current end time, there is conflict
        # If there is a conflict, need one more meeting room
        while start_pointer < len(intervals):
            if start_array[start_pointer] < end_array[end_pointer]:
                meeting_rooms +=1
                start_pointer +=1
            else:
                meeting_rooms -=1
                end_pointer +=1

            result = max(result,meeting_rooms)
        
        return result
    
    #o(nlogn) time, o(n) space


