"""
Problem: Minimum Insertions to Balance a Parentheses String
LeetCode ID: 1541
Pattern: Greedy / Parentheses
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Each opening parenthesis `(` must be matched with exactly two
   consecutive closing parentheses `))`.
2. Maintain `need`, the number of closing parentheses still required
   to balance the opening parentheses processed so far.
3. Maintain `res`, the number of insertions performed.
4. When an opening parenthesis is encountered:
   - Increase `need` by 2 because it requires two closing parentheses.
   - If `need` becomes odd, insert one `)` to complete a previous
     opening parent's required pair, then decrease `need` by 1.
5. When a closing parenthesis is encountered:
   - Decrease `need` by 1 because it satisfies one required closing
     parenthesis.
   - If `need` becomes negative, there was no opening parenthesis
     available to match it. Insert one `(` and set `need` to 1 because
     that new opening parenthesis still requires two closing parentheses,
     one of which is satisfied by the current `)`.
6. After processing the string, insert `need` closing parentheses to
   satisfy all remaining requirements.
7. Return the total number of insertions.
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0  
        need = 0 

        for c in s:
            if c == '(':
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            else:
                need -= 1
                if need == -1:
                    res += 1
                    need = 1  

        return res + need
    