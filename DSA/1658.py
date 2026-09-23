"""
Problem: Minimum Operations to Reduce X to Zero
LeetCode ID: 1658
Pattern: Sliding Window / Prefix Sum
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Instead of removing elements from the left and right to obtain x,
   find the longest contiguous subarray whose sum is:
   total_sum - x.
2. Calculate the target sum:
   target = sum(nums) - x.
3. If target is negative, x is larger than the total sum, so the
   required operations are impossible.
4. If target is zero, the entire array must be removed, so return n.
5. Use a sliding window to find the longest subarray with sum equal
   to target.
6. Since all numbers are positive, whenever the window sum becomes
   greater than target, move the left pointer forward until the
   window becomes valid.
7. If a window has sum equal to target, update the maximum window
   length.
8. The elements outside this longest subarray are exactly the elements
   that must be removed from the two ends.
9. Therefore, the minimum number of operations is:
   n - longest_valid_subarray_length.
"""

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1
        if target == 0:
            return n

        left = 0
        window_sum = 0
        max_len = -1

        for right in range(n):
            window_sum += nums[right]

            while window_sum > target:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else n - max_len