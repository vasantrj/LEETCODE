"""
Problem: Simplify Path
LeetCode ID: 71
Pattern: Stack / String Parsing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Split the path on '/' to get individual tokens.
2. Skip empty tokens and '.', since they do not change the directory.
3. For '..', pop the top of the stack if it is non-empty (move up one level);
   at the root, it is ignored.
4. For any other token (including '...', a valid directory name), push it
   onto the stack.
5. Join the stack with '/' and prepend a leading '/' to form the canonical path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)