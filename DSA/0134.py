
"""
Problem: Gas Station
LeetCode ID: 134
Pattern: Greedy / Arrays
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Calculate the total gas available and total cost required.
2. If total gas is less than total cost, completing the
   circular route is impossible. Return -1.
3. Initialize start = 0 to track the potential starting station.
4. Initialize tank = 0 to track the current fuel balance.
5. Traverse every station and update the tank using:
   gas[i] - cost[i].
6. If the tank becomes negative, the current starting station
   cannot reach the next station.
7. Set the next station (i + 1) as the new starting point
   and reset the tank to zero.
8. Return the final starting station index.
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start