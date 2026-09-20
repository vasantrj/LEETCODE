"""
Problem: Maximum Number of Vowels in a Substring of Given Length
LeetCode ID: 1456
Pattern: Sliding Window / String
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Store all vowels in a set for constant-time membership checks.
2. Count the number of vowels in the first substring of length k.
   This becomes the initial sliding window.
3. Store this count as the current maximum.
4. Slide the window one character at a time:
   - Add the new character entering the window if it is a vowel.
   - Remove the character leaving the window if it is a vowel.
5. Update the maximum vowel count after each window shift.
6. If the maximum reaches k, the substring contains only vowels,
   so no better result is possible and we can stop early.
7. Return the maximum number of vowels found in any substring of
   length k.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cur = sum(1 for c in s[:k] if c in vowels)
        best = cur
        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i - k] in vowels:
                cur -= 1
            best = max(best, cur)
            if best == k:
                break
        return best

        