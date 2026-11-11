
"""
Problem: Minimum Cost to Acquire Required Items
LeetCode ID: 3789
Pattern: Greedy / Mathematical Optimization
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Define a helper function f(k), where k represents the
   number of times the combined item is purchased.
2. The combined purchase costs k * costBoth.
3. After purchasing k combined items, calculate the remaining
   individual requirements:
   max(0, need1 - k) and max(0, need2 - k).
4. Add the individual purchase costs to obtain the total cost.
5. Evaluate three possibilities:
   - Purchase no combined items: k = 0.
   - Purchase enough combined items to satisfy need1: k = need1.
   - Purchase enough combined items to satisfy need2: k = need2.
6. Return the minimum cost among these three possibilities.
"""

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def f(k):
            return k * costBoth + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2

        return min(f(0), f(need1), f(need2))