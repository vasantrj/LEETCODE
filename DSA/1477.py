"""
Problem: Find Two Non-overlapping Sub-arrays Each With Target Sum
LeetCode ID: 1477
Pattern: Sliding Window / Prefix Minimum
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Since the array contains positive integers, use a sliding window to
   find every subarray whose sum equals target.
2. Maintain:
   - left: left boundary of the current sliding window.
   - total: sum of elements inside the current window.
   - min_len_so_far: shortest valid subarray found so far.
   - prefix_min[i]: shortest valid subarray ending at or before index i.
3. Expand the window by moving right and adding arr[right] to total.
4. While total is greater than target, shrink the window from the left.
5. When total equals target:
   - Compute the current subarray length.
   - If there is a valid subarray completely before the current one,
     combine its minimum length with the current length.
   - Update the overall minimum answer.
   - Update min_len_so_far with the current subarray length.
6. Store min_len_so_far in prefix_min[right] so future subarrays can
   efficiently find the shortest valid subarray before them.
7. Return the minimum combined length if two non-overlapping subarrays
   exist; otherwise, return -1.
"""


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        prefix_min = [INF] * n
        left = 0
        total = 0
        min_len_so_far = INF
        ans = INF
        
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            
            if total == target:
                cur_len = right - left + 1
                if left > 0 and prefix_min[left - 1] != INF:
                    ans = min(ans, cur_len + prefix_min[left - 1])
                min_len_so_far = min(min_len_so_far, cur_len)
            
            prefix_min[right] = min_len_so_far
        return ans if ans != INF else -1