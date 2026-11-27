"""
Problem: Maximum Number of Items From Sale I
LeetCode ID: 3946
Pattern: Dynamic Programming / 0-1 Knapsack
Difficulty: Medium
Time Complexity: O(n * K + n * budget), K = number of distinct factors
Space Complexity: O(budget)

Approach:
1. Buying item i for price_i yields cnt_i copies: the purchased copy plus a
   free copy of every item j where factor_j % factor_i == 0 (item i counts itself).
2. Free copies of a type only count once across different first purchases,
   so each item's first purchase is a 0-1 knapsack choice with
   weight price_i and value cnt_i.
3. Let dp[j] be the max copies from first purchases costing at most j.
   Iterate j downward so each item is used at most once.
4. Leftover budget (budget - i) buys plain copies of the cheapest item,
   giving (budget - i) // mn extra copies.
5. Return the maximum of dp[i] + (budget - i) // mn over all i.
"""


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = Counter(f for f, _ in items)
        mn = min(p for _, p in items)

        dp = [0] * (budget + 1)
        for fac, price in items:
            cnt = sum(v for k, v in freq.items() if k % fac == 0)
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + cnt)

        return max(dp[i] + (budget - i) // mn for i in range(budget + 1))
    