# leetcode 1029
# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

# sending the person to the city A, the company would lose price_A - price_B, which could negative or positive.
# sort the values by priceA - priceB
# the value at the beginning of the sorted array will be the minimum cost price A value
# the value at the end of the sorted array will be the minimum cost price B value
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        total = 0
        end = len(costs)
        for i in range(end // 2):
            total += costs[i][0] + costs[end - i -1][1]
        return total
