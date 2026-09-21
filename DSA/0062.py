"""
Problem: Unique Paths
LeetCode ID: 62
Pattern: Combinatorics / Dynamic Programming
Difficulty: Medium
Time Complexity: O(min(m, n))
Space Complexity: O(1)

Approach:
1. A robot must move from the top-left corner to the bottom-right
   corner of an m x n grid.
2. To reach the destination, it must make exactly:
   - m - 1 downward moves.
   - n - 1 rightward moves.
3. The total number of moves is therefore:
   (m - 1) + (n - 1) = m + n - 2.
4. The problem becomes choosing which m - 1 of these moves are
   downward (or equivalently, which n - 1 are rightward).
5. The number of possible paths is given by the binomial coefficient:
   C(m + n - 2, m - 1).
6. Use Python's built-in comb() function to calculate this value
   directly.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)