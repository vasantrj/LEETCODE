"""
Problem: Nearest Exit from Entrance in Maze
LeetCode ID: 1926
Pattern: Breadth-First Search / Grid / Shortest Path
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Treat each open cell `.` as a node in a grid graph, with edges to
   its four adjacent open cells.
2. Mark the entrance as visited immediately so that BFS does not return
   to it or consider it as an exit.
3. Use BFS starting from the entrance, storing the current distance
   from the entrance along with each cell.
4. For every neighboring open cell:
   - If it lies on the boundary, it is an exit. Because BFS explores
     cells in increasing distance order, the first boundary cell found
     is the nearest exit.
   - Otherwise, mark it visited and add it to the queue.
5. If BFS finishes without reaching any boundary cell, return `-1`.
"""


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        sr, sc = entrance
        maze[sr][sc] = '+'     
        q = deque([(sr, sc, 0)])

        while q:
            r, c, d = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if nr in (0, m - 1) or nc in (0, n - 1):
                        return d + 1   
                    maze[nr][nc] = '+' 
                    q.append((nr, nc, d + 1))
        return -1
        