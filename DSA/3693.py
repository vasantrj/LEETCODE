
"""
Problem: Climbing Stairs II
LeetCode ID: 3693
Pattern: Dynamic Programming
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Create a DP array where dp[j] represents the minimum
   cost required to reach stair j.
2. Initialize dp[0] = 0 because reaching the ground
   requires no cost.
3. Initialize all other DP values to infinity.
4. Iterate through every stair from 1 to n.
5. For each stair, consider three possible jump lengths:
   1, 2, and 3.
6. If the previous stair position is valid, calculate
   the transition cost:
   dp[j-k] + k*k + costs[j-1].
7. Update dp[j] with the minimum cost among all valid jumps.
8. Return dp[n] as the minimum cost to reach the top.
"""

from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float('inf')] * n
        for j in range(1, n + 1):
            for k in (1, 2, 3):
                if j - k >= 0:
                    dp[j] = min(dp[j], dp[j - k] + k * k + costs[j - 1])
        return dp[n]