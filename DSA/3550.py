"""
Problem: Smallest Index With Digit Sum Equal to Index
LeetCode ID: 3550
Pattern: Array / Digit Manipulation
Difficulty: Easy
Time Complexity: O(n * d)
Space Complexity: O(1)

Approach:
1. Traverse the array while keeping track of each element's index.
2. For every number, calculate its digit sum using repeated division
   by 10:
   - The last digit is obtained using x % 10.
   - Remove the last digit using x //= 10.
3. Compare the calculated digit sum with the current index.
4. Since the array is traversed from left to right, the first index
   where the digit sum equals the index is automatically the smallest.
5. Return that index immediately.
6. If no index satisfies the condition, return -1.
"""

from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            digit_sum = 0

            while num:
                digit_sum += num % 10
                num //= 10

            if digit_sum == index:
                return index

        return -1