"""
Problem: Rotting Oranges
LeetCode ID: 994
Pattern: Breadth-First Search / Multi-Source BFS / Grid
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Traverse the grid and:
   - Add every rotten orange to the queue as a starting point.
   - Count the total number of fresh oranges.
2. Use multi-source BFS so that all initially rotten oranges spread the
   rot simultaneously.
3. Process the queue level by level, where each BFS level represents
   one minute.
4. For every rotten orange, inspect its four adjacent cells.
5. If an adjacent cell contains a fresh orange:
   - Mark it as rotten.
   - Decrease the fresh-orange count.
   - Add it to the queue so it can spread the rot during the next minute.
6. Continue until either there are no more rotten oranges to process or
   all fresh oranges have become rotten.
7. If fresh oranges remain, return `-1`; otherwise, return the number of
   minutes required.
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1),):
                    nr, nc = r + dr, c + dc

                    if ( 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return -1 if fresh else minutes