"""
Problem: Equal Row and Column Pairs
LeetCode ID: 2352
Pattern: Hash Map / Matrix
Difficulty: Medium
Time Complexity: O(n²)
Space Complexity: O(n²)

Approach:
1. Convert every row of the grid into a tuple so it can be used as
   a hashable key.
2. Use a Counter to store the frequency of each unique row.
3. Use zip(*grid) to efficiently obtain every column as a tuple.
4. For each column, look up its frequency in the row Counter.
5. Add these frequencies together to count every matching
   row-column pair.
6. Since duplicate rows or columns can occur, their frequencies
   naturally account for all valid pairs.
"""


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        return sum(rows[column] for column in zip(*grid))