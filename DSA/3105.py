
"""
Problem: Longest Strictly Increasing or Strictly Decreasing Subarray
LeetCode ID: 3105
Pattern: Arrays / Greedy / Single Pass
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize best, inc, and dec to 1 because every
   individual element forms a valid subarray of length 1.
2. Traverse the array starting from the second element.
3. If the current element is greater than the previous element:
   - Increment the increasing subarray length.
   - Reset the decreasing length to 1.
4. If the current element is smaller than the previous element:
   - Increment the decreasing subarray length.
   - Reset the increasing length to 1.
5. If both elements are equal, reset both lengths to 1.
6. Update best with the maximum of the current increasing
   and decreasing lengths.
7. Return best as the longest monotonic subarray length.
"""


from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best