
"""
Problem: Minimum Changes to Make K Semi-palindromes
LeetCode ID: 2911
Pattern: Dynamic Programming / Divisors / String Processing
Difficulty: Hard
Time Complexity: O(n^4 + k * n^2)
Space Complexity: O(n^2 + k * n)

Approach:
1. Generate all possible divisors for every substring length.
   A valid semi-palindrome must have a divisor d such that
   d is smaller than the substring length and divides it.
2. Create a cost table where cost[i][j] stores the minimum
   character changes required to make s[i:j+1] a semi-palindrome.
3. For every substring, examine all valid divisors.
4. For each divisor d, compare characters belonging to
   corresponding residue classes modulo d.
5. Count mismatched character pairs. Each mismatch requires
   one character change to make the pair equal.
6. Store the minimum mismatch count across all valid divisors.
7. Use dynamic programming where dp[j][i] represents the
   minimum changes needed to divide the first i characters
   into exactly j semi-palindromic substrings.
8. Try every valid previous partition position p and update:
   dp[j][i] = min(dp[j-1][p] + cost[p][i-1]).
9. Return dp[k][n] as the minimum number of changes required.
"""

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        divs = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for L in range(2 * d, n + 1, d):
                divs[L].append(d)

        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divs[L]:
                    c = 0
                    for r in range(d):
                        lo = i + r
                        hi = j - d + 1 + r
                        while lo < hi:
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                    if c < best:
                        best = c
                cost[i][j] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):
                best = INF
                for p in range(2 * (j - 1), i - 1):
                    v = dp[j - 1][p] + cost[p][i - 1]
                    if v < best:
                        best = v
                dp[j][i] = best

        return dp[k][n]