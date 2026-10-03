"""
Problem: Longest Valid Parentheses
LeetCode ID: 32
Pattern: Stack / String / Parentheses
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a stack to store indices of unmatched opening parentheses and
   the index of the most recent unmatched closing parenthesis.
2. Initialize the stack with `-1` as a sentinel index. This represents
   the position immediately before the beginning of a potential valid
   substring.
3. For every character:
   - If it is `(`, push its index onto the stack.
   - If it is `)`, pop the most recent index because this closing
     parenthesis attempts to match an opening parenthesis.
4. If the stack becomes empty after popping, the current closing
   parenthesis cannot be matched. Push its index as the new boundary.
5. Otherwise, the substring from `stack[-1] + 1` to the current index
   is valid, so its length is `i - stack[-1]`.
6. Keep track of the maximum valid length encountered.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] 
        best = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])

        return best
    