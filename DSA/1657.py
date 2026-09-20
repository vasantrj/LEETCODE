"""
Problem: Determine if Two Strings Are Close
LeetCode ID: 1657
Pattern: Hash Map / Frequency Counting
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. If the two strings have different lengths, they cannot be made
   equal using the allowed operations, so return False.
2. Count the frequency of every character in both strings using
   Counter.
3. The two strings must contain exactly the same set of characters.
   This is required because the allowed operations cannot introduce
   a character that does not already exist.
4. Compare the sorted frequency values of both strings.
5. The frequency values only need to match as a multiset because
   operation 1 allows swapping any two existing characters'
   frequencies.
6. If both the character sets and frequency multisets are equal,
   the strings can be transformed into each other.
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())