# leetcode 269
# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
# sorted lexicographically by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".
# Otherwise, return a string of the unique letters in the new alien language sorted 
# in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

# this solution will require topoolgical sort which requires a Directed Acyclical Graph (DAG)
# use a postorder dfs traversal to get all of the children of the parent node all the way up to the parent
# once you have all the letters, we want to reverse it, to have them in order

# for loop detection, mark if a node has already been visited,by adding it to a dictionary

# time complexity O(n) with n being the size of characters in the words list in the input

class Solution:
    def alienOrder(self, words: List[str]) -> str:
    # create adjacency list of ordering of the characters loop through every char in words
        adj = {c:set() for w in words for c in w} # use a set to ensure no duplicates

        for i in range(len(words)-1): #use minus one so we can get a pair of words every time
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1),len(word2))
            # handle invalid edge case where two words have the same prefix
            # but word1 is longer than word2 which means they are not sorted in ordering
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for j in range(minLen): # go through each character between the two words
                # try to find first differing character
                if word1[j] != word2[j]:
                    # add differing character to word1's adjacency list because this char must come after the current char lexicographically
                    adj[word1[j]].add(word2[j])
                    break

        # now the adjaceny list is filled, we can perform postorder dfs
        # visited set,False means character has been visited, True means visited and in current path
        # if the char is not in visited, it has not been visited yet
        visited = {} 
        result = []

        def dfs(c): # dfs function takes in current character
            if c in visited:
                return visited[c] #if this returns true, we have detected a loop

            visited[c] = True # add char to visited, and set it to True, in current path

            for neighbor in adj[c]: # go through every character that's a neighbor of c and run dfs on its
                if dfs(neighbor):
                    return True # if you detect a loop, return True

            visited[c] = False # change char's value to false bc its no longer in current path
            result.append(c)

        for c in adj:
            if dfs(c): # if loop detected, return 
                return ""
        result.reverse() # reverse the result array becuase postorder, put it in reverse        
        return "".join(result) # finally, join the reversed array and return the string


