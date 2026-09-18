"""
Problem: Min Cost Climbing Stairs
LeetCode ID: 746
Pattern: Dynamic Programming
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. We can start from either step 0 or step 1, and the goal is to reach
   the top beyond the last index.
2. Let dp[i] represent the minimum cost required to reach step i.
3. To reach step i, we can come from either:
   - Step i - 1, paying cost[i - 1].
   - Step i - 2, paying cost[i - 2].
4. Therefore, the recurrence is:
       dp[i] = min(
           dp[i - 1] + cost[i - 1],
           dp[i - 2] + cost[i - 2]
       )
5. The base cases are dp[0] = 0 and dp[1] = 0 because we can start from
   either of the first two steps without paying a cost.
6. Only the previous two DP values are needed, so store them in prev1
   and prev2 instead of maintaining a complete DP array.
7. After processing step n, prev1 contains the minimum cost to reach
   the top.
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev2, prev1 = 0, 0
        for i in range(2, n + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2, prev1 = prev1, curr
        return prev1
    