"""
Problem: Merge Intervals
LeetCode ID: 56
Pattern: Arrays / Sorting / Greedy
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Sort all intervals by their starting values.
2. Initialize result with the first interval.
3. Traverse the remaining intervals:
   - Compare the current interval's start with the end of the last
     interval in result.
   - If start <= last_end, the intervals overlap:
     - Extend the end of the last interval to the larger of the two
       ending values.
   - Otherwise, the intervals do not overlap, so add the current
     interval to result.
4. Continue until all intervals have been processed.
5. Return the merged intervals.
"""


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
        
        return result
    