# leetcode 1048
# You are given an array of words where each word consists of lowercase English letters.
# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
# Return the length of the longest possible word chain with words chosen from the given list of words.

# sort the list to have smallest length strings first
# go through every possible predecessor by removing each char from the string
# store the max of the current strings in a hashmap 
# add 1 to the max of the possible predecessors (take this value from hashmap)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        maxLen = 0

        # Sorting the list in terms of the word length.
        words.sort(key=lambda x: len(x))

        longest = 1

        for word in words:
            presentLength = 1
            # Find all possible predecessors for the current word by removing one letter at a time.
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                #checks every single predecessor's dp value and only takes the maximum possible (if pred is not in dp hashmap, gets zero)
                previousLength = dp.get(predecessor, 0)
                presentLength = max(presentLength, previousLength + 1)
            dp[word] = presentLength
            longest = max(longest, presentLength)

        return longest


    

        