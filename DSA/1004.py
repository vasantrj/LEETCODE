"""
Problem: Max Consecutive Ones III
LeetCode ID: 1004
Pattern: Sliding Window / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Maintain a sliding window using two pointers, left and right.
2. Expand the window by moving right through the array.
3. Keep track of the number of zeros inside the current window.
4. If the number of zeros becomes greater than k, the window is
   invalid because more than k zeros would need to be flipped.
5. Shrink the window from the left until it contains at most k zeros.
6. For every valid window, calculate its length and update the
   maximum length found.
7. Each element enters and leaves the window at most once, giving
   an O(n) time solution.
"""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0
        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best