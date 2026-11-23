"""
Problem: Product of the Last K Numbers
LeetCode ID: 1352
Pattern: Prefix Product / Design
Difficulty: Medium
Time Complexity: add() O(1), getProduct() O(1)
Space Complexity: O(n)

Approach:
1. Maintain a prefix product list, where prefix[i] is the product of all
   numbers added since the last zero (prefix[0] = 1 acts as a sentinel).
2. When a 0 is added, every product spanning it becomes 0, so reset the
   list to [1]. Earlier numbers no longer matter.
3. For getProduct(k), if k >= len(prefix), the last k numbers include a zero
   (the list only holds numbers added after the most recent zero), so
   return 0.
4. Otherwise, the product of the last k numbers is
   prefix[-1] // prefix[-1 - k], since dividing out the earlier prefix
   leaves exactly the last k values.
"""

class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]