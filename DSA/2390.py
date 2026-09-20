"""
Problem: Removing Stars From a String
LeetCode ID: 2390
Pattern: Stack / String
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a stack to store characters that have not been removed.
2. Traverse the string from left to right.
3. If the current character is not a star, add it to the stack.
4. If the current character is a star, remove the most recently
   added character from the stack using pop().
5. This works because every star removes the closest non-star
   character to its left.
6. Finally, join the remaining characters in the stack to construct
   the resulting string.
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)