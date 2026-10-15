
"""
Problem: Minimum Number of Arrows to Burst Balloons
LeetCode ID: 452
Pattern: Greedy / Interval Scheduling
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space, excluding sorting

Approach:
1. Sort the balloons by their ending coordinates in ascending order.
2. Shoot the first arrow at the end coordinate of the first balloon.
3. Iterate through the remaining balloons.
4. If a balloon starts at or before the current arrow position,
   the existing arrow bursts it, so no additional arrow is needed.
5. If a balloon starts after the current arrow position, shoot
   another arrow at its ending coordinate and increment the count.
6. Return the total number of arrows required.
"""


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        arrows = 1
        pos = points[0][1]
        for start, end in points[1:]:
            if start > pos:
                arrows += 1
                pos = end
        return arrows
