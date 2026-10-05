"""
Problem: Score of Parentheses
LeetCode ID: 856
Pattern: Stack / Parentheses
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a stack where each element stores the score accumulated inside
   the corresponding level of parentheses.
2. Start with `0` on the stack to represent the score outside all
   parentheses.
3. When an opening parenthesis `(` is encountered, push `0` onto the
   stack to start a new nested group.
4. When a closing parenthesis `)` is encountered:
   - Pop the score `v` of the current group.
   - If `v == 0`, the group is `()`, which has a score of 1.
   - Otherwise, the group is nested and its score is `2 * v`.
5. Add the calculated score to the parent level on the stack.
6. After processing the complete string, `stack[0]` contains the total
   score of the entire balanced parentheses string.
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                value = stack.pop()
                stack[-1] += max(2 * value, 1)

        return stack[0]