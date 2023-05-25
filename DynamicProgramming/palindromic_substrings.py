#leetcode #647
#Given a string s, return the number of palindromic substrings in it.

class Solution:
    def countSubstrings(self, s: str) -> int:
        #very similar approach to leetcode #5
        #start l and r pointers at the middle index (i) and expand from there for odd palindromes
        #start l = i and r = i+1 for even palindromes
        #increment count everytime s[l] == s[r]
        count = 0
        for i in range(len(s)):
            count += self.count_palindrome(s,i,i) #for odd length palindromes
            count += self.count_palindrome(s,i,i+1) #for even length palindromes
        return count

    #use a helper function to do the counting
    def count_palindrome(self,s,left,right):
        count = 0
        while (left >= 0 and right < len(s)) and (s[left] == s[right]):
            count+=1
            left -=1
            right+=1
        return count
    
#O(n^2) time and O(1) space