
"""
Problem: Minimum Moves to Equal Array Elements II
LeetCode ID: 462
Pattern: Sorting / Median
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space (excluding sorting)

Approach:
1. Sort the array in ascending order.
2. Use two pointers, one at the beginning and one at the end.
3. Pair the smallest and largest elements.
4. Add their difference to the result. This represents the
   minimum moves needed to bring that pair to a common value.
5. Move both pointers toward the center.
6. Continue until the pointers meet or cross.
7. Return the accumulated number of moves.
"""


from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        return res

    