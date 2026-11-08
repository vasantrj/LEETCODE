"""
Problem: Count Servers that Communicate
LeetCode ID: 1267
Pattern: Matrix / Counting
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(m + n)

Approach:
1. Get the number of rows (m) and columns (n) in the grid.
2. Create two arrays to count the servers in each row and column.
3. Traverse the grid and increment the corresponding row and
   column counts whenever a server (1) is found.
4. Traverse the grid again.
5. For every server, check whether its row contains more than
   one server or its column contains more than one server.
6. If either condition is true, the server can communicate
   with at least one other server. Increment the result.
7. Return the total number of communicating servers.
"""


from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    res += 1

        return res