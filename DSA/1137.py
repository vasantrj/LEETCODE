"""
Problem: N-th Tribonacci Number
LeetCode ID: 1137
Pattern: Dynamic Programming / Math
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. The Tribonacci sequence is defined as:
       T0 = 0
       T1 = 1
       T2 = 1
       Tn = Tn-1 + Tn-2 + Tn-3
2. Handle the base cases directly:
   - If n == 0, return 0.
   - If n == 1 or n == 2, return 1.
3. Maintain three variables:
   - a stores Tn-3.
   - b stores Tn-2.
   - c stores Tn-1.
4. For every value from 3 through n, calculate the next Tribonacci
   number as a + b + c.
5. Shift the three variables forward so they represent the next three
   consecutive values.
6. Return c after the loop, which contains Tn.
7. Only three values are maintained, avoiding the need for a complete
   DP array.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c