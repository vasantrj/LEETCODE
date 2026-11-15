
"""
Problem: Minimum Size Subarray Sum
LeetCode ID: 209
Pattern: Sliding Window / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize left = 0 to represent the starting index
   of the sliding window.
2. Maintain window_sum to track the sum of the current window.
3. Initialize min_len to infinity to store the minimum
   valid subarray length.
4. Expand the window by iterating through nums using right.
5. Add each current element to window_sum.
6. While window_sum is greater than or equal to target:
   - Update min_len with the current window length.
   - Remove the leftmost element from window_sum.
   - Move left forward to shrink the window.
7. Continue until every element has been processed.
8. Return min_len if a valid subarray exists; otherwise,
   return 0.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len