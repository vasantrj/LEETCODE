"""
Problem: Evaluate the Bracket Pairs of a String
LeetCode ID: 1807
Pattern: Hashing / String Parsing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Store all key-value pairs from `knowledge` in a hash map for O(1)
   average-time lookups.
2. Traverse the string from left to right using an index `i`.
3. When an opening parenthesis `(` is encountered:
   - Find the corresponding closing parenthesis `)`.
   - Extract the key between the parentheses.
   - Look up the key in the hash map.
   - Append its value to the result, or `?` if the key is unknown.
   - Move `i` to the character immediately after `)`.
4. If the current character is not `(`, append it directly to the result.
5. Join all collected pieces at the end to construct the final string.
"""


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {k: v for k, v in knowledge}
        result = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i+1:j]
                result.append(mapping.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)
    