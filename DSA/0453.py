
"""
Problem: Minimum Moves to Equal Array Elements
LeetCode ID: 453
Pattern: Arrays / Mathematical Observation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Observe that incrementing n - 1 elements by one is equivalent
   to decrementing the remaining element by one.
2. Instead of simulating the operations, consider making every
   element equal to the minimum element.
3. Each element nums[i] requires nums[i] - min(nums) moves.
4. Sum the required moves for all elements.
5. Simplify the expression to:
   sum(nums) - n * min(nums).
6. Return the calculated minimum number of moves.
"""

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)