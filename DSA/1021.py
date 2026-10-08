"""
Problem: Remove Outermost Parentheses
LeetCode ID: 1021
Pattern: String / Parentheses / Depth Tracking
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Maintain `depth` to track the current nesting depth of parentheses.
2. Traverse the string from left to right.
3. When an opening parenthesis `(` is encountered:
   - If the current depth is greater than 0, it is not an outermost
     parenthesis, so add it to the result.
   - Then increase the depth.
4. When a closing parenthesis `)` is encountered:
   - First decrease the depth because this parenthesis closes the current
     nested level.
   - If the resulting depth is greater than 0, the closing parenthesis
     belongs to an inner level, so add it to the result.
5. The first `(` and matching final `)` of every primitive parentheses
   string are therefore excluded.
6. Join the collected characters to construct the final string.
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:
                    res.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(ch)
        return ''.join(res)
    