
"""
Problem: Maximum K to Sort a Permutation
LeetCode ID: 3644
Pattern: Bit Manipulation / Bitwise AND
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize ans to -1, which acts as an all-bits-set mask
   for the non-negative integers in the permutation.
2. Traverse nums with each element x and its target index i.
3. If x already equals i, the element is in its correct position
   and does not affect the result.
4. Otherwise, update ans using bitwise AND with x.
5. If every element is already correctly positioned, ans remains -1,
   so return 0. Otherwise, return ans.
"""


class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            if x != i:
                ans &= x

        return 0 if ans == -1 else ans
