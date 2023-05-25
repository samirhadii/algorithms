# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# 'Z' -> "26"

#Given a string s containing only digits, return the number of ways to decode it.

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_previous = 1
        one_previous = 1

        for i in range(1,len(s)): #start at the second char, because we have initialized the first char as 1 already
            cur = 0
            if s[i] != "0": #any single digit other than zero is valid
                cur = one_previous
            #find the possible two digit number and see if it is valid
            possible_two_digit = int(s[i-1:i+1]) #i-1 inclusive and i+1 is exclusive
            if possible_two_digit >9 and possible_two_digit < 27:
                cur+=two_previous
            #update the variables per iteration
            two_previous = one_previous
            one_previous = cur

        return one_previous #the number stored in one_previous will land on the final answer

#O(N) time complexity
#O(1) space complexity 