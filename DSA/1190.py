"""
Problem: Reverse Substrings Between Each Pair of Parentheses
LeetCode ID: 1190
Pattern: Stack / String Manipulation
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(n)

Approach:
1. Use a stack where each element represents the characters collected
   inside the current level of parentheses.
2. Start with an empty list for the outermost level.
3. When an opening parenthesis `(` is encountered, push a new empty list
   onto the stack to begin collecting characters for that nested substring.
4. When a closing parenthesis `)` is encountered:
   - Pop the characters belonging to the current parenthesized substring.
   - Reverse those characters.
   - Append the reversed substring to the previous level.
5. For normal characters, append them to the list at the top of the stack.
6. After processing the entire string, join the characters in the
   outermost list to form the final result.
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                top = stack.pop()
                top.reverse()
                stack[-1].extend(top)
            else:
                stack[-1].append(ch)
        return ''.join(stack[0])