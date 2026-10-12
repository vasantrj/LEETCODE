
"""
Problem: Apply Operations on Array to Maximize Sum of Squares
LeetCode ID: 2897
Pattern: Greedy / Bit Manipulation
Difficulty: Medium
Time Complexity: O(30 * (n + k))
Space Complexity: O(1) auxiliary space

Approach:
1. Count how many numbers in nums have each of the 30 bits set.
2. Construct k numbers greedily, setting each bit in the current
   number whenever that bit still has a positive count.
3. Decrease the count of every bit used in the current number.
4. This concentrates available set bits into fewer numbers, maximizing
   the sum of their squares.
5. Add each constructed number's square to the answer modulo 10^9 + 7.
"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 30
        for x in nums:
            for b in range(30):
                if x >> b & 1:
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(30):
                if cnt[b] > 0:
                    cnt[b] -= 1
                    cur |= 1 << b
            ans = (ans + cur * cur) % MOD
        return ans