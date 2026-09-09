"""
Problem: Count Commas in Range II
LeetCode ID: 3871
Pattern: Math / Counting
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. A comma appears in a number whenever the number reaches a power
   of 1000, such as 1,000, 1,000,000, and so on.
2. Start with the first comma threshold, 1000.
3. For each threshold:
   - Every number from threshold through n contains a comma at that
     position.
   - Therefore, it contributes n - threshold + 1 commas.
4. Multiply the threshold by 1000 to move to the next comma position.
5. Continue until the threshold becomes greater than n.
6. Return the total number of commas counted across all positions.
"""


class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        threshold = 1000
        while threshold <= n:
            total += n - threshold + 1
            threshold *= 1000
        return total