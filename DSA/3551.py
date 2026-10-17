
"""
Problem: Minimum Swaps to Sort by Digit Sum
LeetCode ID: 3551
Pattern: Sorting / Cycle Detection
Difficulty: Medium
Time Complexity: O(n log n + n * D)
Space Complexity: O(n)

Approach:
1. Define digit_sum() to calculate the sum of digits of a number.
2. Sort the original indices using (digit_sum(nums[i]), nums[i])
   as the sorting key, following the problem's tie-breaking rule.
3. Treat the sorted index order as a permutation of the original
   positions.
4. Use a visited array to identify permutation cycles.
5. For each unvisited cycle of size s, add s - 1 to the swap count,
   because that many swaps are needed to place all elements correctly.
6. Return the total number of swaps.
"""

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or order[i] == i:
                continue
            j, size = i, 0
            while not visited[j]:
                visited[j] = True
                j = order[j]
                size += 1
            swaps += size - 1
        return swaps
    