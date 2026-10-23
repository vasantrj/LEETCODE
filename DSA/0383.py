
"""
Problem: Ransom Note
LeetCode ID: 383
Pattern: Arrays / Frequency Counting
Difficulty: Easy
Time Complexity: O(m + n)
Space Complexity: O(1)

Approach:
1. If ransomNote is longer than magazine, return False because
   there are not enough characters to construct the note.
2. Create a frequency array of size 26 for lowercase English letters.
3. Count the occurrences of each character in magazine.
4. Traverse ransomNote and decrement the corresponding character
   count for every required character.
5. If any count becomes negative, magazine does not contain enough
   occurrences of that character, so return False.
6. If all characters are available, return True.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = [0] * 26

        for ch in magazine:
            counts[ord(ch) - ord("a")] += 1

        for ch in ransomNote:
            i = ord(ch) - ord("a")
            counts[i] -= 1

            if counts[i] < 0:
                return False

        return True