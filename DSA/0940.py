"""
Problem: Distinct Subsequences II
LeetCode ID: 940
Pattern: Dynamic Programming / Strings / Hashing
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(k)

Approach:
1. Let dp represent the number of distinct subsequences including
   the empty subsequence for the characters processed so far.
2. Initially, dp = 1 because the empty string is one subsequence.
3. For each character c in s:
   - Every existing subsequence can either include or exclude c,
     which would give 2 * dp subsequences.
   - Some subsequences are counted twice because c has appeared before.
   - last[c] stores the dp value from before the previous occurrence
     of c, so subtracting last[c] removes these duplicates.
4. Update last[c] with the old dp value before processing c.
5. The final dp includes the empty subsequence, so subtract 1 to
   return only non-empty distinct subsequences.
6. Apply modulo 10^9 + 7 to prevent the count from becoming too large.
"""

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last = {}
        dp = 1
        for char in s:
            old_dp = dp
            dp = (2 * dp - last.get(char, 0)) % MOD
            last[char] = old_dp
        return (dp - 1) % MOD