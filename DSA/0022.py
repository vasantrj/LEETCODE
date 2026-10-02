"""
Problem: Generate Parentheses
LeetCode ID: 22
Pattern: Backtracking / Recursion / Parentheses
Difficulty: Medium
Time Complexity: O(4^n / sqrt(n))
Space Complexity: O(n)

Approach:
1. Generate all valid combinations using backtracking.
2. Maintain two counters:
   - `open_count`: number of `(` used so far.
   - `close_count`: number of `)` used so far.
3. An opening parenthesis can be added only when `open_count < n`.
4. A closing parenthesis can be added only when `close_count < open_count`.
   This guarantees that no prefix contains more closing parentheses than
   opening parentheses.
5. Store the current combination in `path` and use backtracking to explore
   both valid choices.
6. When the path length reaches `2 * n`, the combination contains exactly
   `n` opening and `n` closing parentheses, so add it to the result.
7. After each recursive call, remove the added parenthesis from `path`
   to restore the previous state.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []

        def backtrack(open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return res