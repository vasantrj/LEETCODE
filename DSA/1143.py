
"""
Problem: Longest Common Subsequence
LeetCode ID: 1143
Pattern: Dynamic Programming / Space Optimization
Difficulty: Medium
Time Complexity: O(m * n)
Space Complexity: O(n)

Approach:
1. Swap the strings if necessary so text2 is the shorter string,
   minimizing the space required for the DP arrays.
2. Initialize prev with zeros to represent LCS lengths when
   one string is empty.
3. Iterate through each character of text1 and create a current
   DP row for the current character.
4. If the characters match, set cur[j] = prev[j - 1] + 1.
5. Otherwise, take the maximum of prev[j] and cur[j - 1].
6. Replace prev with cur after processing each row and return
   the final LCS length.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur
        return prev[n]
