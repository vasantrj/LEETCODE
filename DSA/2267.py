"""
Problem: Check if There Is a Valid Parentheses String Path
LeetCode ID: 2267
Pattern: Dynamic Programming / Grid DP / Bitset
Difficulty: Hard
Time Complexity: O(m * n * (m + n))
Space Complexity: O(n * (m + n))

Approach:
1. A valid parentheses path must start with `(` and end with `)`.
   Also, the total number of cells in the path must be even so that
   parentheses can be balanced.
2. For each cell, maintain a bitset representing all possible balance
   values that can be reached at that cell.
3. The bit at position `k` represents that a path can reach the current
   cell with a parenthesis balance of `k`.
4. A cell can be reached from either:
   - The cell directly above it.
   - The cell directly to its left.
   Combine both possibilities using bitwise OR.
5. If the current cell contains `(`, shift the bitset left by one because
   the balance increases by 1.
6. If the current cell contains `)`, shift the bitset right by one because
   the balance decreases by 1.
7. Use a one-dimensional DP array because each cell only depends on the
   current value from above and the already-updated value from the left.
8. At the bottom-right cell, check whether balance 0 is reachable.
   Bit 0 being set means a valid path exists.
"""


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cur = 1  
                else:
                    cur = 0
                    if i > 0:
                        cur |= dp[j]   
                    if j > 0:
                        cur |= dp[j - 1] 

                if grid[i][j] == '(':
                    cur <<= 1  
                else:
                    cur >>= 1  
                dp[j] = cur

        return dp[n - 1] & 1 == 1  
        