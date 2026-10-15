
"""
Problem: Subarrays Distinct Element Sum of Squares I
LeetCode ID: 2913
Pattern: Arrays / Hash Set / Brute Force
Difficulty: Easy
Time Complexity: O(n^2) expected
Space Complexity: O(n)

Approach:
1. Iterate through every possible starting index i.
2. Initialize an empty set to track distinct elements in the
   subarray beginning at index i.
3. Extend the subarray one element at a time using index j.
4. Add nums[j] to the set, automatically maintaining unique elements.
5. Calculate the square of the set's size and add it to total
   for every subarray considered.
6. Return total after processing all possible subarrays.
"""


from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                total += len(seen) ** 2
        return total

