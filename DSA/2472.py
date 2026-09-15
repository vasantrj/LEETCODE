"""
Problem: Maximum Number of Non-overlapping Palindrome Substrings
LeetCode ID: 2472
Pattern: Dynamic Programming / Strings / Palindrome
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(n^2)

Approach:
1. Build a 2D boolean table is_pal where is_pal[i][j] indicates
   whether the substring s[i..j] is a palindrome.
2. Fill the table from right to left:
   - Every single character is a palindrome.
   - A substring is a palindrome if its first and last characters
     are equal and its inner substring is also a palindrome.
3. Use a 1D DP array where dp[i] represents the maximum number of
   non-overlapping valid palindromic substrings that can be selected
   from the first i characters of s.
4. For every position i:
   - Skip the current character by setting dp[i] = dp[i - 1].
   - Check substrings ending at i - 1 with lengths k and k + 1.
   - If such a substring is a palindrome, select it and update
     dp[i] = max(dp[i], dp[j] + 1).
5. Only lengths k and k + 1 need to be checked because if a palindrome
   has length greater than k, an appropriate sub-palindrome of length
   k or k + 1 can be selected without decreasing the maximum count.
6. Return dp[n], which represents the maximum number of valid
   non-overlapping palindrome substrings in the entire string.
"""



class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            isPal[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True
        
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  
            for length in (k, k + 1):
                j = i - length
                if j >= 0 and isPal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]