
"""
Problem: Spiral Matrix
LeetCode ID: 54
Pattern: Matrix / Simulation
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(1) auxiliary space (excluding output)

Approach:
1. Initialize four boundaries: top, bottom, left, and right.
2. Traverse the top row from left to right, then move the top boundary down.
3. Traverse the right column from top to bottom, then move the right boundary left.
4. If rows remain, traverse the bottom row from right to left and move the bottom boundary up.
5. If columns remain, traverse the left column from bottom to top and move the left boundary right.
6. Repeat until all boundaries cross, ensuring every element is visited exactly once.
7. Return the result containing elements in spiral order.
"""


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Left to right along the top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # Top to bottom along the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Right to left along the bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # Bottom to top along the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res