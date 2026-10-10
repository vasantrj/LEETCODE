"""
Problem: Minimum Sum of Squared Difference
LeetCode ID: 2333
Pattern: Greedy / Counting / Frequency Array
Difficulty: Medium
Time Complexity: O(n + M), where M is the maximum absolute difference
Space Complexity: O(n + M)

Approach:
1. Calculate the absolute difference between corresponding elements
   of `nums1` and `nums2`.
2. Combine `k1` and `k2` into `k`, representing the total number of
   operations available to reduce these differences.
3. If the sum of all differences is at most `k`, every difference can
   be reduced to zero, so return 0.
4. Build a frequency array `cnt`, where `cnt[d]` represents how many
   elements currently have an absolute difference of `d`.
5. Process difference values from the maximum down to 1:
   - If enough operations are available to reduce every difference at
     level `i` by one, move all those elements to level `i - 1`.
   - Otherwise, use the remaining operations to move only `k` elements
     down by one level, then stop.
6. This greedy strategy reduces the largest differences first, which
   minimizes the sum of squared differences.
7. Calculate the final answer by summing `count * difference²` for
   every difference level.
"""

from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diffs) <= k:
            return 0

        mx = max(diffs)
        cnt = [0] * (mx + 1)
        for d in diffs:
            cnt[d] += 1

        for i in range(mx, 0, -1):
            if cnt[i] == 0:
                continue
            if k >= cnt[i]:
                k -= cnt[i]
                cnt[i - 1] += cnt[i]
                cnt[i] = 0
            else:
                cnt[i] -= k
                cnt[i - 1] += k
                k = 0
                break

        return sum(c * i * i for i, c in enumerate(cnt))