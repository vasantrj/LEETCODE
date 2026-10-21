
"""
Problem: Minimum Operations to Sort a String
LeetCode ID: 3863
Pattern: Greedy / String
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Check whether the string is already sorted. If so, return 0.
2. If the string has length 2 and is not sorted, return -1 because
   sorting cannot be achieved using the permitted operations.
3. Find the minimum and maximum characters in the string.
4. If the first character is the minimum or the last character
   is the maximum, return 1.
5. Otherwise, if a minimum character appears before the last
   position or a maximum character appears after the first position,
   return 2.
6. If none of these conditions hold, return 3.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if s == "".join(sorted(s)):
            return 0

        if n == 2:
            return -1

        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1

        if mn in s[:-1] or mx in s[1:]:
            return 2

        return 3
