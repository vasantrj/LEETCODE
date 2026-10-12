
"""
Problem: House Robber
LeetCode ID: 198
Pattern: Dynamic Programming / Space Optimization
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain two variables, prev and cur, representing the maximum
   money that can be robbed up to the previous two positions.
2. For each house with money x, choose between:
   - Skipping the current house and keeping cur.
   - Robbing the current house and adding x to prev.
3. Update prev and cur simultaneously to preserve the previous
   dynamic programming states.
4. Return cur as the maximum money that can be robbed without
   robbing two adjacent houses.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for x in nums:
            prev, cur = cur, max(cur, prev + x)
        return cur
