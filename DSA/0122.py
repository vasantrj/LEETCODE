
"""
Problem: Best Time to Buy and Sell Stock II
LeetCode ID: 122
Pattern: Greedy / Arrays
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize profit to zero.
2. Iterate through the prices starting from the second day.
3. Compare the current day's price with the previous day's price.
4. If the current price is higher, calculate the positive
   difference between the two prices.
5. Add this difference to the total profit.
6. Repeat for every day and return the accumulated profit.

This approach captures every profitable upward price movement,
allowing multiple buy and sell transactions.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
