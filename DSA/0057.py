"""
Problem: Insert Interval
LeetCode ID: 57
Pattern: Arrays / Intervals / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Initialize an empty result list and use a pointer i to traverse
   the sorted intervals.
2. Add all intervals that end before the new interval starts:
   - These intervals cannot overlap with newInterval.
3. Process all intervals that overlap with newInterval:
   - Update the start of newInterval to the smaller start value.
   - Update the end of newInterval to the larger end value.
4. Add the merged newInterval to the result.
5. Add all remaining intervals because they start after the merged
   interval and cannot overlap with it.
6. Return the resulting list of non-overlapping intervals.
"""


from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result