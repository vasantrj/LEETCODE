
"""
Problem: Domino and Tromino Tiling
LeetCode ID: 790
Pattern: Dynamic Programming / Space Optimization
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Handle the base cases: for n = 1, there is 1 tiling;
   for n = 2, there are 2 tilings.
2. Use the recurrence relation:
   f(n) = (2 * f(n - 1) + f(n - 3)) % MOD.
3. Maintain three variables representing the previous three
   DP states instead of storing the entire DP array.
4. Iterate from 3 through n, updating the states using the
   recurrence relation.
5. Return the final state modulo 10^9 + 7.
"""

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n <= 2:
            return n
        a, b, c = 1, 1, 2
        for _ in range(3, n + 1):
            a, b, c = b, c, (2 * c + a) % MOD
        return c