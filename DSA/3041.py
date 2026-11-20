
"""
Problem: Maximize Consecutive Elements in an Array After Modification
LeetCode ID: 3041
Pattern: Dynamic Programming / Sorting / Hash Map
Difficulty: Hard
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Sort the array so elements are processed in non-decreasing order.
2. Use a hash map dp where dp[v] stores the maximum length of a
   consecutive sequence ending at value v.
3. For each element x, consider two possibilities:
   - Increase x by 1: extend the sequence ending at x.
   - Keep x unchanged: extend the sequence ending at x - 1.
4. Update both DP states using the best available previous sequence.
5. Return the maximum value stored in the DP map.
"""

from typing import List
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        for x in nums:
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1
        return max(dp.values())
