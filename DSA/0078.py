"""
Problem: Subsets
LeetCode ID: 78
Pattern: Arrays / Backtracking / Bit Manipulation
Difficulty: Medium
Time Complexity: O(n * 2^n)
Space Complexity: O(n * 2^n)

Approach:
1. Start with result containing the empty subset.
2. Traverse each number in nums.
3. For the current number:
   - Take every subset already present in result.
   - Create a new subset by adding the current number to it.
   - Add all newly created subsets to result.
4. Every existing subset generates exactly one new subset that
   includes the current number.
5. After processing all numbers, result contains all 2^n possible
   subsets.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result