"""
Problem: Remove Palindromic Subsequences
LeetCode ID: 1332
Pattern: String / Palindrome
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If the string is empty, no subsequences need to be removed, so return 0.
2. Check whether the entire string is a palindrome by comparing it with
   its reversed version.
3. If the entire string is a palindrome, it can be removed in one operation,
   so return 1.
4. If the string is not a palindrome, note that the string contains only
   the characters 'a' and 'b'.
5. We can remove all 'a' characters as one palindromic subsequence and all
   'b' characters as another palindromic subsequence.
6. Therefore, any non-empty string that is not already a palindrome can
   always be removed in exactly 2 operations.
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2