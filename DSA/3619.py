
"""
Problem: Count Islands With Total Value Divisible by K
LeetCode ID: 3619
Pattern: Grid / Graph Traversal / Iterative DFS
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Traverse every cell in the grid.
2. When a positive cell is found, start an iterative DFS to explore
   its entire connected island using four-directional movement.
3. Add each visited cell's value to the island's total.
4. Mark each visited cell as zero to avoid processing it again.
5. After exploring the complete island, check whether its total
   is divisible by k.
6. Increment the count if the island's total is divisible by k.
7. Return the total number of qualifying islands.
"""


from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = 0
                    stack = [(i, j)]
                    total += grid[i][j]
                    grid[i][j] = 0 

                    while stack:
                        x, y = stack.pop()
                        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                total += grid[nx][ny]
                                grid[nx][ny] = 0
                                stack.append((nx, ny))

                    if total % k == 0:
                        count += 1

        return count
