"""
Problem: Circle and Rectangle Overlapping
LeetCode ID: 1401
Pattern: Geometry / Math
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Find the point inside or on the boundary of the rectangle that is
   closest to the circle's center.
2. For the x-coordinate:
   - If xCenter is inside [x1, x2], use xCenter.
   - Otherwise, use the nearest rectangle boundary.
3. Do the same for the y-coordinate using [y1, y2].
4. Calculate the horizontal and vertical distances between the circle
   center and this nearest point:
       dx = xCenter - nearest_x
       dy = yCenter - nearest_y
5. The squared distance between the circle center and the nearest
   rectangle point is:
       dx² + dy²
6. The circle overlaps the rectangle if this squared distance is less
   than or equal to radius².
7. Squared distances are used to avoid computing a square root.
"""


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        return dx * dx + dy * dy <= radius * radius