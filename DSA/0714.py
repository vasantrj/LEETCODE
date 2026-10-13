
"""
Problem: Best Time to Buy and Sell Stock with Transaction Fee
LeetCode ID: 714
Pattern: Dynamic Programming / State Machine
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain two states:
   - cash: Maximum profit when not holding a stock.
   - hold: Maximum profit when holding a stock.
2. Initialize cash to 0 because no transactions have been made,
   and hold to -prices[0] because buying the first stock costs money.
3. For each subsequent price, update hold by either keeping the
   existing stock or buying at the current price using cash.
4. Update cash by either keeping the existing profit or selling
   the stock at the current price and paying the transaction fee.
5. Return cash, which represents the maximum profit without
   holding a stock at the end.
"""


from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            hold = max(hold, cash - p)
            cash = max(cash, hold + p - fee)
        return cash

