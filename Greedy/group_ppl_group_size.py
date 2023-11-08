# leetcode 1282
# group people given the group size they belong to

# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. 
# For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
# Return a list of groups such that each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group, and every person must be in a group. 
# If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        output = []
        for i in range(len(groupSizes)):
            cur_group = groupSizes[i]
            groups[cur_group].append(i)
            if len(groups[cur_group]) >= cur_group:
                output.append(groups[cur_group])
                groups[cur_group] = []
        return output

# greedy approach
# uses O(N) space and O(N) time