# Write a function to crush candy in one dimensional board. In candy crushing games,
# groups of like items are removed from the board. In this problem, any sequence of 3 or more like items
# should be removed and any items adjacent to that sequence should now be considered adjacent to each other.
# This process should be repeated as many time as possible.
# return shortest possible string after removal


# greedy removal doesn't find shortest
def greedy(s: str) -> str:
    # use a stack to store occurances and counts together [char,num_of_occurances]
    stack = []
    for char in s:
        # check the top of the stack and add 1 to the frequency if this is a repeat.
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:  # else if this is the first encounter, add it to the stack with a value of 1 bc we've seen it once
            stack.append([char, 1])
        # if the frequency of the occurances equals k, pop all of them
        if stack[-1][1] == 3:
            stack.pop()

    output = ""
    for chars, freq in stack:
        output += chars * freq
    return output


# find shortest string after removal
def recursiveBestCandyCrush(s):
    def recursion(s, i):
        for i in range(i, len(s)):
            if (
                i + 2 < len(s)
                and i + 1 < len(s)
                and s[i] == s[i + 1]
                and s[i] == s[i + 2]
            ):
                j = i
                i += 2

                repeated = s[i]
                while i < len(s) and s[i] == repeated:
                    i += 1

                left = s[:j]
                right = s[i:]
                left += right

                uncrushed = recursion(s, i)
                crushed = recursion(left, 0)

                return uncrushed if len(uncrushed) < len(crushed) else crushed

        return s

    return recursion(s, 0)


# greedy solution
input_str1 = "aaabbbc"
print("greedy candy crush: ", greedy(list(input_str1)))  # Output: "c"

# optimal recursive solution for shortest output
s2 = "aaaaabbbacd"
print("Recursive Best Candy Crush:", recursiveBestCandyCrush(s2))  # returns "cd"
