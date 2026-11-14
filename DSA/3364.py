
"""
Problem: Minimum Positive Sum Subarray
LeetCode ID: 3364
Pattern: Prefix Sum / Array
Difficulty: Easy
Time Complexity: O(n * (r - l + 1))
Space Complexity: O(n)

Approach:
1. Calculate the prefix sum array where pre[i] stores
   the sum of elements before index i.
2. Initialize best to infinity to track the minimum
   positive subarray sum.
3. Iterate through every possible starting index i.
4. For each starting index, consider subarray lengths
   from l to r.
5. Calculate the ending index j = i + length.
6. If j exceeds the array length, stop checking longer
   subarrays for the current starting index.
7. Calculate the subarray sum in O(1) using:
   pre[j] - pre[i].
8. If the sum is positive, update best with the minimum
   positive sum found so far.
9. Return best if a valid positive sum exists;
   otherwise, return -1.
"""


class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x
        best = float('inf')
        for i in range(n):
            for length in range(l, r + 1):
                j = i + length
                if j > n:
                    break
                s = pre[j] - pre[i]
                if s > 0:
                    best = min(best, s)
        return -1 if best == float('inf') else best