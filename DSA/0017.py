"""
Problem: Letter Combinations of a Phone Number
LeetCode ID: 17
Pattern: Backtracking / Recursion
Difficulty: Medium
Time Complexity: O(4^n * n)
Space Complexity: O(n) auxiliary space, excluding output

Approach:
1. If the input `digits` is empty, return an empty list because there
   are no combinations to generate.
2. Create a mapping from each digit (2–9) to its corresponding letters
   on a telephone keypad.
3. Use backtracking to build combinations one character at a time.
4. At each recursive call, use index `i` to identify the current digit.
5. For every letter mapped to that digit:
   - Append the letter to `path`.
   - Recursively process the next digit.
   - Remove the letter after returning to explore other possibilities.
6. When `i` reaches the length of `digits`, the current path contains
   one complete combination. Join it into a string and add it to the result.
7. Return all generated combinations.
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        res, path = [], []

        def backtrack(i: int) -> None:
            if i == len(digits):
                res.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res