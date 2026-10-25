
"""
Problem: Number of Closed Islands
LeetCode ID: 1254
Pattern: Grid / Graph Traversal / Iterative DFS
Difficulty: Medium
Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)

Approach:
1. Define sink() to iteratively traverse a connected region of land
   (cells containing 0) and convert its cells to water (1).
2. Traverse the grid's borders and sink every land region connected
   to a border, since these regions cannot be closed islands.
3. Initialize the closed-island count to zero.
4. Visit the interior cells of the grid.
5. Whenever an unvisited land cell (0) is found, increment the count
   and sink its entire connected region.
6. Return the count of remaining closed islands.
"""


from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def sink(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < rows
                        and 0 <= ny < cols
                        and grid[nx][ny] == 0
                    ):
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if (
                    r in (0, rows - 1) or c in (0, cols - 1)
                ) and grid[r][c] == 0:
                    sink(r, c)

        count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    count += 1
                    sink(r, c)

        return count