#leetcode 139

#Given a string s and a dictionary of strings wordDict,
#return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#words from wordDict can be reused multiple times in segmentation

#every character in the string must be used

#Iterate bottom-up starting from the last index and caching if word break is possible at each index
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         
         dp = [False] * (len(s) + 1) # plus one for the base case, out of bounds of input string
         dp[len(s)] = True

         #iterate through the input string backwards
         for i in range(len(s),-1,-1):
              #check every word in wordDict at the starting position i
              for w in wordDict:
                   if (i+len(w)) <= len(s) and s[i:i+ len(w)] == w: #if this is true, we in bounds and safe to compare and we perform the compare
                       dp[i] = dp[i + len(w)]
                   if dp[i]:
                        break
         return dp[0]