"""
Problem: Reverse Degree of a String
LeetCode ID: 3498
Pattern: String / Character Mapping
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Traverse the string from left to right using 1-based positions.
2. For each character, calculate its reverse alphabetical value:
   - 'a' has reverse value 26.
   - 'b' has reverse value 25.
   - ...
   - 'z' has reverse value 1.
3. The reverse value of a character ch can be calculated as:
   26 - (ord(ch) - ord('a')).
4. Multiply the reverse value by the character's 1-based position.
5. Add each weighted value to the total reverse degree and return
   the final result.
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for position, char in enumerate(s, 1):
            reverse_value = 26 - (ord(char) - ord('a'))
            total += reverse_value * position
        return total