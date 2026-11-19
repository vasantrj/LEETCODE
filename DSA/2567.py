
"""
Problem: Minimum Score by Changing Two Elements
LeetCode ID: 2567
Pattern: Greedy / Sorting
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space (excluding sorting)

Approach:
1. Sort the array in ascending order.
2. We can change at most two elements to minimize the difference
   between the maximum and minimum values.
3. Consider the three optimal possibilities:
   - Change the two smallest elements: nums[-1] - nums[2].
   - Change the smallest and largest elements: nums[-2] - nums[1].
   - Change the two largest elements: nums[-3] - nums[0].
4. Calculate the score for all three possibilities.
5. Return the minimum score.
"""

class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(nums[-3] - nums[0],
                   nums[-2] - nums[1],
                   nums[-1] - nums[2])
                   