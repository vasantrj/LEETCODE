"""
Problem: Backspace String Compare
LeetCode ID: 844
Pattern: Two Pointers / String
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(1)

Approach:
1. Compare both strings from right to left using two pointers.
2. A helper function finds the next valid character index while handling
   backspaces:
   - When '#' is encountered, increase the skip count.
   - When a normal character is encountered and skip > 0, skip that
     character and decrease the skip count.
   - Stop when a character remains that is not affected by any backspace.
3. For both strings, repeatedly find their next valid characters.
4. If both valid characters exist, compare them:
   - If they are different, the strings are not equal.
5. If only one string has a valid character remaining, the strings are
   not equal.
6. Move both pointers one position backward and continue.
7. If all valid characters match, return True.
8. The comparison is performed without constructing the resulting strings,
   so only constant extra space is used.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_char_index(string, index):
            skip = 0

            while index >= 0:
                if string[index] == "#":
                    skip += 1
                    index -= 1
                elif skip > 0:
                    skip -= 1
                    index -= 1
                else:
                    break

            return index

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = next_valid_char_index(s, i)
            j = next_valid_char_index(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True