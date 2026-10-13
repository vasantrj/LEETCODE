
"""
Problem: Edit Distance
LeetCode ID: 72
Pattern: Dynamic Programming / Space Optimization
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(n)

Approach:
1. Let m and n be the lengths of word1 and word2.
2. Initialize the previous DP row so that converting an empty
   string into the first j characters of word2 requires j insertions.
3. For each character in word1, initialize the current row's first
   element to i, representing i deletions to form an empty string.
4. If the current characters match, carry forward the diagonal
   value from the previous row.
5. Otherwise, take one plus the minimum of:
   - prev[j]: Delete a character.
   - curr[j - 1]: Insert a character.
   - prev[j - 1]: Replace a character.
6. Update the previous row after each iteration and return
   the final DP value.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))   

        for i in range(1, m + 1):
            curr = [i] + [0] * n   
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min( prev[j], curr[j - 1], prev[j - 1])
            prev = curr
        return prev[n]
        