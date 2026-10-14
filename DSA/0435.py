
"""
Problem: Non-overlapping Intervals
LeetCode ID: 435
Pattern: Greedy / Interval Scheduling
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space, excluding sorting

Approach:
1. Sort intervals by their ending times in ascending order.
2. Initialize removed to zero and prev_end to negative infinity.
3. Iterate through the sorted intervals.
4. If the current interval starts at or after prev_end,
   keep it and update prev_end to its ending time.
5. Otherwise, the current interval overlaps with a previously
   kept interval, so increment removed.
6. Return removed, the minimum number of intervals to remove
   to make the remaining intervals non-overlapping.
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
        return removed
