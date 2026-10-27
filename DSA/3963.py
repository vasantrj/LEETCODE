
"""
Problem: Create Grid With Exactly One Path
LeetCode ID: 3963
Pattern: Grid Construction / Graph Theory
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Initialize an m x n grid filled with walls ('#').
2. Open the first column by replacing every cell in that column
   with '.'.
3. Open the entire last row by replacing every cell in that row
   with '.'.
4. Convert each row into a string and return the resulting list.
5. This creates an L-shaped open corridor from the top-left to
   the bottom-right, ensuring exactly one path between them.
"""


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        for i in range(m):
            grid[i][0] = '.'

        grid[m - 1] = ['.'] * n
        return ["".join(row) for row in grid]
