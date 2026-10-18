
"""
Problem: Number of Ways to Reorder Array to Get Same BST
LeetCode ID: 1569
Pattern: Binary Search Tree / Combinatorics / Recursion
Difficulty: Hard
Time Complexity: O(n^2)
Space Complexity: O(n^2)

Approach:
1. Treat the first element of each array as the BST root.
2. Partition the remaining elements into left and right subarrays
   based on whether they are smaller or greater than the root.
3. Recursively calculate the number of valid reorderings for
   the left and right subtrees.
4. Count the ways to interleave both subtree sequences while
   preserving their internal orders using C(n - 1, len(left)).
5. Multiply the interleaving count by the number of valid
   reorderings of both subtrees, applying modulo 10^9 + 7.
6. Subtract one to exclude the original ordering.
"""

from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        def ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return comb(len(arr) - 1, len(left)) % MOD * ways(left) % MOD * ways(right) % MOD
        return (ways(nums) - 1) % MOD
        