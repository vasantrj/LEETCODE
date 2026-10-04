"""
Problem: Valid Parenthesis String
LeetCode ID: 678
Pattern: Greedy / Parentheses
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain a range of possible open-parenthesis counts while scanning
   the string:
   - `lo` = minimum possible number of unmatched `(`.
   - `hi` = maximum possible number of unmatched `(`.
2. For an opening parenthesis `(`, both bounds increase by 1 because it
   must be treated as an opening parenthesis.
3. For a closing parenthesis `)`, both bounds decrease by 1 because it
   must close an opening parenthesis.
4. For `*`, consider all three possibilities:
   - `*` as `(` → increase the maximum.
   - `*` as `)` → decrease the minimum.
   - `*` as empty → keep the current balance.
   Therefore, update `lo -= 1` and `hi += 1`.
5. If `hi` becomes negative, even the most optimistic interpretation
   cannot produce a valid prefix, so return `False`.
6. The minimum possible balance can never be negative, so clamp `lo`
   to zero after every character.
7. At the end, if `lo == 0`, there is at least one interpretation that
   produces a balanced parenthesis string.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0
    