
"""
Problem: Game of Life
LeetCode ID: 289
Pattern: Matrix / In-place State Transition
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(1)

Approach:
1. Traverse every cell and count its eight neighboring live cells.
2. Use temporary values to represent both the current and next states:
   - 0: Dead -> Dead
   - 1: Live -> Live
   - 2: Live -> Dead
   - 3: Dead -> Live
3. When counting live neighbors, treat values 1 and 2 as originally alive.
   This ensures that temporary updates do not affect neighbor calculations.
4. Apply the Game of Life rules:
   - A live cell dies if it has fewer than two or more than three live neighbors.
   - A dead cell becomes alive if it has exactly three live neighbors.
5. After processing every cell, use modulo 2 to convert temporary states
   into their final values.
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                live = 0

                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue

                        r, c = i + di, j + dj

                        if 0 <= r < m and 0 <= c < n:
                            if board[r][c] in (1, 2):
                                live += 1

                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 2  # Live -> Dead
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 3  # Dead -> Live

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
