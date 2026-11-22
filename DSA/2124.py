
"""
Problem: Check if All A's Appears Before All B's
LeetCode ID: 2124
Pattern: String / Linear Scan
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. All occurrences of 'a' must appear before any occurrence of 'b'.
2. If the substring "ba" exists, a 'b' appears before an 'a',
   violating the required order.
3. Check whether "ba" is absent from the string.
4. Return True if it is absent; otherwise, return False.
"""

class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s