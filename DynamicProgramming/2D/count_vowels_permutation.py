# leetcode 1220 Count Vowels Permutation

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.


# recognize that this is a dynammic programming problem becuase there is repeated work with larger words
# only returning the count not the actual combos
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[j][c] = num of strings of length=j
        # the last character is c
        dp = [
            [],
            [1, 1, 1, 1, 1],
        ]  # initialize an empty array at dp[0] array because there are zero strings at length zero
        # intialize dp[1] to be all ones becuase we know from example 1, if n=1 then we only have 1 possibility per character, we will solve the rest until n

        a, e, i, o, u = 0, 1, 2, 3, 4  # map each vowel to an index in dp subarrays
        mod = 10**9 + 7  # mod value for question requirements

        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])  # append some dummy values to dp array

            dp[j][a] = (
                dp[j - 1][e] + dp[j - 1][i] + dp[j - 1][u]
            ) % mod  # "a" can go after e,i,u so get their previous values
            dp[j][e] = (dp[j - 1][a] + dp[j - 1][i]) % mod  # "e" can go after a & i
            dp[j][i] = (dp[j - 1][e] + dp[j - 1][o]) % mod  # i can go after e & o
            dp[j][o] = dp[j - 1][i]  # o can go after i. no addition so no need to mod
            dp[j][u] = dp[j - 1][o] + dp[j - 1][i]  # u can go after o & i

        # finally, return the sum of the values in the last entry of the dp array
        return sum(dp[n]) % mod
