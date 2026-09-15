"""
Problem: Number of Lines To Write String
LeetCode ID: 806
Pattern: Simulation / String
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Each character has a predefined width given by the widths array.
2. Start with one line and a current line width of 0.
3. Traverse every character in the string:
   - Convert the character to its corresponding index using
     ord(char) - ord('a').
   - Get the character's width from the widths array.
4. If adding the current character would make the line wider than 100:
   - Start a new line.
   - Set the current line width to the width of the current character.
5. Otherwise, add the character's width to the current line width.
6. Return the total number of lines and the width of the last line.
"""


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current_width = 0
        for char in s:
            char_width = widths[ord(char) - ord("a")]

            if current_width + char_width > 100:
                lines += 1
                current_width = char_width
            else:
                current_width += char_width

        return [lines, current_width]