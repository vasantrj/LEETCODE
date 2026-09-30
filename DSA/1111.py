"""
Problem: Maximum Nesting Depth of Two Valid Parentheses Strings
LeetCode ID: 1111
Pattern: Greedy / Parentheses / Depth Tracking
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Maintain `depth` to track the current nesting depth of the original
   valid parentheses string.
2. Split the parentheses into two groups based on the parity of the
   current depth.
3. When an opening parenthesis `(` is encountered:
   - Increase the current depth.
   - Assign the parenthesis to group `depth % 2`.
4. When a closing parenthesis `)` is encountered:
   - It belongs to the same group as the corresponding opening
     parenthesis, so use the current depth parity.
   - Then decrease the depth.
5. Alternating assignments between the two groups ensure that deeply
   nested parentheses are distributed between them.
6. The resulting two sequences remain valid, while their maximum
   nesting depths are minimized.
"""

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = []
        depth = 0

        for ch in seq:
            if ch == "(":
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1

        return result