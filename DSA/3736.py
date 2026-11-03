"""
Problem: Minimum Moves to Equal Array Elements III
LeetCode ID: 3736
Pattern: Arrays / Mathematical Observation
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Find the maximum element in the array.
2. Use the maximum element as the target value.
3. Each element requires (maximum - element) increments
   to reach the target.
4. Calculate the total moves using:
   (maximum * length of array) - sum of all elements.
5. Return the calculated minimum number of moves.
"""


from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)
    