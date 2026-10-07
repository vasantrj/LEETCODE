"""
Problem: Remove Invalid Parentheses
LeetCode ID: 301
Pattern: Backtracking / DFS / Parentheses
Difficulty: Hard
Time Complexity: O(2^n)
Space Complexity: O(n)

Approach:
1. First determine the minimum number of invalid opening and closing
   parentheses that must be removed:
   - `l` = number of extra `(` that must be removed.
   - `r` = number of extra `)` that must be removed.
2. Use DFS/backtracking to explore whether each parenthesis should be
   removed or kept.
3. For an opening parenthesis `(`:
   - If `l > 0`, explore the option of removing it.
   - Also explore keeping it and increase the current open-parenthesis
     count.
4. For a closing parenthesis `)`:
   - If `r > 0`, explore the option of removing it.
   - It can be kept only when there is an unmatched opening parenthesis
     available.
5. Non-parenthesis characters are always kept.
6. At the end of the string, a valid result is produced only when:
   - No required removals remain.
   - No unmatched opening parentheses remain.
7. Store valid results in a set to eliminate duplicates caused by
   removing identical parentheses from different positions.
8. Because the DFS removes exactly the minimum number of invalid
   parentheses calculated initially, every generated result is valid
   and uses the minimum possible number of removals.
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l: l -= 1
                else: r += 1

        n, res, path = len(s), set(), []

        def dfs(i, l, r, open_):
            if l < 0 or r < 0:
                return
            if i == n:
                if l == r == open_ == 0:
                    res.add(''.join(path))
                return
            c = s[i]
            if c == '(':
                dfs(i + 1, l - 1, r, open_)          
                path.append(c); dfs(i + 1, l, r, open_ + 1); path.pop()  
            elif c == ')':
                dfs(i + 1, l, r - 1, open_)         
                if open_ > 0:                      
                    path.append(c); dfs(i + 1, l, r, open_ - 1); path.pop()
            else:
                path.append(c); dfs(i + 1, l, r, open_); path.pop()

        dfs(0, l, r, 0)
        return list(res)