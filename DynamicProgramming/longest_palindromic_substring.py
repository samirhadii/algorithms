#leetcode number 5
#Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #approach is to expand from the center to find palindromes
        #iterate through every letter and expand using current index as the center to try and find longest palindrome

        #handle basic edge cases
        if s is None or len(s) == 0:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            #index i will serve as the center for the left and right pointers in the helper function
            len_even = self.expand_valid_palindrome(s,i,i+1) #start the right pointer index+1 for the case that the palindrome is even length like "aa"
            len_odd = self.expand_valid_palindrome(s,i,i) #start pointers at same index for odd palindromes like "bab"
            current_len = max(len_even,len_odd)
            longest_len = (end - start)
            if current_len > longest_len:
                start = i - ((current_len -1) //2) #current index MINUS half of current substring length
                end = i + (current_len //2) #current index PLUS half of current substring length 

        
        return s[start:end+1] #return the shortest palindromic substring given the start and end points
        
    
    def expand_valid_palindrome(self,s,left,right): #O(n) function 
        while (left >=0 and right <len(s)) and (s[left] == s[right]):
            left -=1
            right+=1
        return (right-left) - 1 #subtract one here bc right-left is the length of substring after the while loop is violated
    

