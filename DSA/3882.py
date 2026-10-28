"""
Problem: Minimum XOR Path in a Grid
LeetCode ID: 3882
Pattern: Dynamic Programming / Bitmask State
Difficulty: Medium
Time Complexity: O(m * n * S)  (S = 1024, the number of possible XOR values)
Space Complexity: O(m * n * S)

Approach:
1. Grid values are bounded (< 1024), so every XOR along a path stays within [0, 1023].
2. Define dp[i][j][x] = True if some path from (0, 0) to (i, j) has XOR equal to x.
3. Base case: dp[0][0][grid[0][0]] = True.
4. Transition: for each cell (i, j) with value v, if XOR x is reachable from the
   top (i-1, j) or the left (i, j-1), then x ^ v is reachable at (i, j).
5. Only moves right and down are allowed, so each cell depends on two neighbors.
6. At the bottom-right cell, scan x from 0 upward and return the first reachable
   value, which is the minimum XOR.
"""
    

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        SIZE = 1024

        dp = [[[False] * SIZE for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j]
                for x in range(SIZE):
                    if (i > 0 and dp[i-1][j][x]) or (j > 0 and dp[i][j-1][x]):
                        dp[i][j][x ^ v] = True

        for x in range(SIZE):
            if dp[m-1][n-1][x]:
                return x