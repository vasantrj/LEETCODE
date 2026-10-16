
"""
Problem: Subarrays Distinct Element Sum of Squares II
LeetCode ID: 2916
Pattern: Segment Tree / Lazy Propagation / Prefix Contributions
Difficulty: Hard
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Maintain a segment tree over possible subarray starting indices.
   Each leaf stores the distinct-element count for a subarray
   ending at the current index.
2. Store two values per segment:
   - s: Sum of distinct-element counts.
   - sq: Sum of squares of distinct-element counts.
3. For each new element at index j, find its previous occurrence p.
   Its distinct-element contribution increases by one for all
   subarrays starting in the range [p + 1, j].
4. Apply a range increment using lazy propagation. If every value
   in a segment increases by k, update its squared sum using:
   sq = sq + 2 * k * s + k * k * segment_length.
5. Update the last occurrence of the current element.
6. Add the root's squared sum to the answer for each ending index,
   taking the result modulo 10^9 + 7.
"""


from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        s = [0] * (4 * n)
        sq = [0] * (4 * n)
        lz = [0] * (4 * n)

        def apply(o, ln, k):
            sq[o] = (
                sq[o] + 2 * k * s[o] + k * k * ln
            ) % MOD
            s[o] = (s[o] + k * ln) % MOD
            lz[o] += k

        def update(o, l, r, L, R):
            if L <= l and r <= R:
                apply(o, r - l + 1, 1)
                return

            m = (l + r) >> 1

            if lz[o]:
                apply(2 * o, m - l + 1, lz[o])
                apply(2 * o + 1, r - m, lz[o])
                lz[o] = 0

            if L <= m:
                update(2 * o, l, m, L, R)

            if R > m:
                update(2 * o + 1, m + 1, r, L, R)

            s[o] = (s[2 * o] + s[2 * o + 1]) % MOD
            sq[o] = (sq[2 * o] + sq[2 * o + 1]) % MOD

        last = {}
        ans = 0

        for j, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, j)
            last[x] = j
            ans = (ans + sq[1]) % MOD

        return ans
