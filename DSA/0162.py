"""
Problem: Find Peak Element
LeetCode ID: 162
Pattern: Binary Search
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Initialize `lo` and `hi` to the first and last indices of the array.
2. While `lo < hi`, calculate the middle index.
3. Compare `nums[mid]` with `nums[mid + 1]`:
   - If `nums[mid] < nums[mid + 1]`, the array is rising at this
     position, so a peak must exist to the right. Set `lo = mid + 1`.
   - Otherwise, the array is falling or reaches a peak at `mid`, so
     keep the left half by setting `hi = mid`.
4. Repeat until `lo == hi`. This index identifies a peak element.
5. Return the index without searching the entire array.

"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        return lo