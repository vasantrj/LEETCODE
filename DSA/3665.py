
"""
Problem: Twisted Mirror Path Count
LeetCode ID: 3665
Pattern: Dynamic Programming / Grid DP / State Transition
Difficulty: Hard
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Approach:
1. Maintain two DP matrices:
   - R[i][j]: Number of paths reaching cell (i, j) moving right.
   - D[i][j]: Number of paths reaching cell (i, j) moving down.
2. Initialize the starting cell (0, 0) with one possible path.
3. For an ordinary cell (grid[i][j] == 0), propagate all incoming
   paths to the right and downward.
4. For a twisted mirror cell (grid[i][j] == 1), swap the directions:
   paths arriving from the rightward state move downward, while
   paths arriving from the downward state move rightward.
5. Apply modulo 10^9 + 7 during every state update.
6. Return the sum of both directional states at the destination.
"""


class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * n for _ in range(m)]  
        D = [[0] * n for _ in range(m)]  

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    total = 1
                    R_in, D_in = 0, 0
                else:
                    R_in, D_in = R[i][j], D[i][j]
                    total = (R_in + D_in) % MOD

                if grid[i][j] == 0:
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + total) % MOD
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + total) % MOD
                else:
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + R_in) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + D_in) % MOD

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD