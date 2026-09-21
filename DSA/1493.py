"""
Problem: Longest Subarray of 1's After Deleting One Element
LeetCode ID: 1493
Pattern: Sliding Window / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use a sliding window with left and right pointers.
2. Maintain the number of zeros inside the current window.
3. Expand the window by moving the right pointer through the array.
4. Since exactly one element must be deleted, the window can contain
   at most one zero.
5. If the window contains more than one zero, move the left pointer
   forward until the window becomes valid again.
6. For every valid window, the number of ones remaining after deleting
   one element is `right - left`.
7. Update the maximum value found and return it after processing the
   entire array.
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        best = 0
        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left)
        return best
    