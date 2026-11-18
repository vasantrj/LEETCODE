
"""
Problem: Minimum Number of Changes to Make Binary String Beautiful
LeetCode ID: 2914
Pattern: Greedy / String
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. A beautiful binary string must be divided into even-length substrings
   containing only identical characters.
2. Since the string length is even, we can optimally divide it into
   consecutive pairs: (0, 1), (2, 3), and so on.
3. Each pair must contain identical characters.
4. If the two characters in a pair differ, exactly one change is needed
   to make them equal.
5. Count all mismatched pairs and return the total number of changes.
"""


class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
        