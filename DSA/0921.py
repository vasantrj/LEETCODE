"""
Problem: Minimum Add to Make Parentheses Valid
LeetCode ID: 921
Pattern: Greedy / Parentheses
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain `open_count` to track the number of unmatched opening
   parentheses encountered so far.
2. Traverse the string from left to right.
3. When an opening parenthesis `(` is encountered, increment
   `open_count`.
4. When a closing parenthesis `)` is encountered:
   - If there is an unmatched opening parenthesis, use it to match the
     closing parenthesis by decrementing `open_count`.
   - Otherwise, this closing parenthesis has no matching opening
     parenthesis, so one `(` must be added. Increment `add`.
5. After processing the entire string, any remaining unmatched opening
   parentheses require one `)` each.
6. Therefore, the minimum number of additions is `add + open_count`.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        add = 0

        for ch in s:
            if ch == "(":
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                add += 1

        return add + open_count