
"""
Problem: Set Matrix Zeroes
LeetCode ID: 73
Pattern: Matrix / In-place Manipulation
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(1)

Approach:
1. Check whether the first row and first column originally contain zeroes.
   Store these conditions separately because they will also be used as markers.
2. Traverse the remaining matrix starting from (1, 1).
3. Whenever a zero is found, mark its corresponding row and column by
   setting matrix[i][0] and matrix[0][j] to zero.
4. Traverse the remaining matrix again and set a cell to zero if its
   corresponding row marker or column marker is zero.
5. Finally, zero out the first row if it originally contained a zero.
6. Zero out the first column if it originally contained a zero.
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        first_row = any(matrix[0][j] == 0 for j in range(n))
        first_col = any(matrix[i][0] == 0 for i in range(m))

        # Mark rows and columns using the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle the first row and column last
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        if first_col:
            for i in range(m):
                matrix[i][0] = 0
