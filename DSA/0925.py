"""
Problem: Long Pressed Name
LeetCode ID: 925
Pattern: Two Pointers / String
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - i points to the current character in name.
   - j points to the current character in typed.
2. Traverse typed from left to right.
3. If name[i] matches typed[j], it is a normal character match:
   - Move both pointers forward.
4. If the characters do not match, check whether typed[j] is the same
   as the previous character in typed:
   - If yes, it represents a long-pressed character, so move only j.
   - If no, typed cannot be a valid long-pressed version of name.
5. Continue until every character in typed has been processed.
6. Finally, check whether all characters in name were matched.
   If i == n, the typed string is valid; otherwise, return False.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n, m = len(name), len(typed)

        while j < m:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == n