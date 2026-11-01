
"""
Problem: Number of 1 Bits
LeetCode ID: 191
Pattern: Bit Manipulation
Difficulty: Easy
Time Complexity: O(k), where k is the number of set bits
Space Complexity: O(1)

Approach:
1. Initialize a counter to zero.
2. Use the bitwise operation n & (n - 1) to remove
   the rightmost set bit (1) from n.
3. Increment the counter each time a set bit is removed.
4. Repeat until n becomes zero.
5. Return the counter as the total number of set bits.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count