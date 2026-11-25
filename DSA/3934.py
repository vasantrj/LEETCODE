"""
Problem: Smallest Unique Subarray
LeetCode ID: 3934
Pattern: Binary Search on Answer + Rolling Hash
Difficulty: Hard
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Uniqueness is monotone in the length L. If a subarray of length L occurs
   exactly once, extending it by one element (right, or left if it ends the
   array) gives a unique subarray of length L + 1. Length n (the whole
   array) is always unique, so the answer lies in [1, n].
2. Binary search on L. For a candidate L, compute the polynomial rolling
   hash of every window of length L using prefix hashes and powers of a
   random base modulo 2^61 - 1.
3. Count the window hashes. If any hash occurs exactly once, a unique
   subarray of length L exists, so try smaller; otherwise try larger.
4. Return the smallest L for which a unique window exists.

Note: the random base and 61-bit modulus make hash collisions negligible.
A deterministic alternative is a suffix array + LCP, where the shortest
unique subarray starting at suffix i has length max(lcp[i-1], lcp[i]) + 1
(valid only if it fits within the remaining suffix length).
"""

import random
from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        M = (1 << 61) - 1
        B = random.randrange(10**6, M - 1)

        pre = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = (pre[i] * B + x) % M
            pw[i + 1] = pw[i] * B % M

        def has_unique(L: int) -> bool:
            cnt = Counter((pre[i + L] - pre[i] * pw[L]) % M
                          for i in range(n - L + 1))
            return 1 in cnt.values()

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo