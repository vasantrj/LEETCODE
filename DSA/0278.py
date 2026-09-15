"""
Problem: First Bad Version
LeetCode ID: 278
Pattern: Binary Search
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Every version after the first bad version is also bad, so the versions
   follow a monotonic pattern:
   - Good, Good, Good, ..., Bad, Bad, Bad.
2. Use binary search to find the first version that returns True from
   isBadVersion().
3. For each middle version:
   - If mid is bad, it could be the first bad version, so search the left
     half by setting right = mid.
   - If mid is good, the first bad version must be after mid, so set
     left = mid + 1.
4. Continue until left == right. At that point, both pointers identify the
   first bad version.
5. Return left as the first bad version.
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left