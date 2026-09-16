"""
Problem: Number of Sets of K Non-Overlapping Line Segments
LeetCode ID: 1621
Pattern: Combinatorics / Modular Arithmetic
Difficulty: Medium
Time Complexity: O(k)
Space Complexity: O(1)

Approach:
1. A set of k non-overlapping line segments can be represented by choosing
   2k endpoints from an expanded set of n - 1 + k positions.
2. The number of valid sets is therefore:
       C(n - 1 + k, 2k)
3. Let:
   - N = n - 1 + k
   - R = 2k
4. Compute the binomial coefficient using the multiplicative formula:
       C(N, R) = N * (N - 1) * ... * (N - R + 1) / R!
5. Perform all multiplication modulo 10^9 + 7 to keep the values manageable.
6. Since division under modulo requires the modular inverse, compute the
   inverse of R! using Fermat's Little Theorem:
       inverse(R!) = (R!)^(MOD - 2) mod MOD
7. Multiply the numerator by the modular inverse of the denominator and
   return the result.
8. If 2k > n - 1 + k, the required combination is impossible, so return 0.
"""


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        N = n - 1 + k
        R = 2 * k
        if R > N:
            return 0
        numerator = 1
        
        for i in range(R):
            numerator = numerator * (N - i) % MOD
        denominator = 1

        for i in range(1, R + 1):
            denominator = denominator * i % MOD
        inverse_denominator = pow(denominator, MOD - 2, MOD)
        return numerator * inverse_denominator % MOD