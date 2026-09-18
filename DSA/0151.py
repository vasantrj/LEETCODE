"""
Problem: Reverse Words in a String
LeetCode ID: 151
Pattern: String / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use split() to divide the string into individual words.
   - It automatically handles leading, trailing, and multiple spaces.
2. Reverse the order of the words using reversed().
3. Join the reversed words using a single space.
4. This removes unnecessary spaces and produces the required string with
   the words in reverse order.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    