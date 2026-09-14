"""
Problem: Rectangle Overlap
LeetCode ID: 836
Pattern: Geometry / Math
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Represent each rectangle using its left, bottom, right, and top
   coordinates.
2. Two rectangles have a positive overlap along the x-axis if:
   - The smaller right boundary is greater than the larger left boundary.
3. Similarly, they have a positive overlap along the y-axis if:
   - The smaller top boundary is greater than the larger bottom boundary.
4. A valid rectangular overlap exists only when there is positive
   overlap on both the x-axis and y-axis.
5. Return True if both conditions are satisfied; otherwise, return False.
"""


from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        x_overlap = min(x2, x4) > max(x1, x3)
        y_overlap = min(y2, y4) > max(y1, y3)
        return x_overlap and y_overlap