
"""
Problem: Online Stock Span
LeetCode ID: 901
Pattern: Monotonic Stack / Design
Difficulty: Medium
Time Complexity: O(1) amortized per next() call
Space Complexity: O(n)

Approach:
1. Initialize an empty stack to store (price, span) pairs.
2. For each new price, initialize span to 1 to count the current day.
3. While the stack is not empty and its top price is less than
   or equal to the current price, pop that pair.
4. Add the popped span to the current span because those consecutive
   days are also included in the current stock span.
5. Push the current (price, span) pair onto the stack.
6. Return the computed span.
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
