"""
Problem: Brace Expansion II
LeetCode ID: 1096
Pattern: Recursion / Parsing / Set Operations
Difficulty: Hard
Time Complexity: O(N * K^2) approximately, where K is the number of
                 generated intermediate strings
Space Complexity: O(K)

Approach:
1. Parse the expression recursively using three grammar levels:
   - Union: expressions separated by commas.
   - Concatenation: consecutive factors that must be combined.
   - Factor: either a single character or a nested brace expression.
2. For a union, parse each comma-separated expression and take the
   set union of all generated strings.
3. For concatenation, start with the empty string and combine every
   string from the current result with every string from the next factor.
4. For a factor:
   - If it starts with '{', recursively parse the expression inside
     the braces.
   - Otherwise, treat the current character as a single possible string.
5. The parser advances `self.i` through the expression, so nested
   brace expressions are handled naturally.
6. Store intermediate results in sets to automatically remove duplicates.
7. Finally, sort the generated strings lexicographically as required.
"""

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.s = expression
        self.i = 0
        result = self.parse_union()
        return sorted(result)
    
    def parse_union(self):
        sets = [self.parse_concat()]
        while self.i < len(self.s) and self.s[self.i] == ',':
            self.i += 1
            sets.append(self.parse_concat())
        result = set()
        for s in sets:
            result |= s
        return result
    
    def parse_concat(self):
        result = {""}
        while self.i < len(self.s) and self.s[self.i] not in ',}':
            factor = self.parse_factor()
            result = {a + b for a in result for b in factor}
        return result
    
    def parse_factor(self):
        if self.s[self.i] == '{':
            self.i += 1 
            inner = self.parse_union()
            self.i += 1 
            return inner
        else:
            c = self.s[self.i]
            self.i += 1
            return {c}