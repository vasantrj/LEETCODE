"""
Problem: Sum of Squares of Special Elements
LeetCode ID: 2778
Pattern: Arrays / Math
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Find the length `n` of the input array.
2. An element at 1-based index `i` is special if `n` is divisible by `i`.
3. Iterate through all 1-based indices from 1 to `n`.
4. For each index that divides `n` evenly, square the corresponding
   element `nums[i - 1]` and include it in the sum.
5. Return the total of all squared special elements.
"""

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum( nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0 )
    