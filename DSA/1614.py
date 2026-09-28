"""
Problem: Maximum Nesting Depth of the Parentheses
LeetCode ID: 1614
Pattern: String / Parentheses / Counting
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain `depth` to represent the current number of open parentheses.
2. Traverse the string from left to right.
3. When an opening parenthesis `(` is encountered, increase `depth`.
4. Update `max_depth` after increasing the current depth.
5. When a closing parenthesis `)` is encountered, decrease `depth`.
6. Characters other than parentheses do not affect the depth.
7. The largest value reached by `depth` is the maximum nesting depth.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for ch in s:
            if ch == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            elif ch == ")":
                depth -= 1

        return max_depth