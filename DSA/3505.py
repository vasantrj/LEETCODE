
"""
Problem: Minimum Operations to Make Elements Within K Subarrays Equal
LeetCode ID: 3505
Pattern: Sliding Window / Two Heaps / Dynamic Programming
Difficulty: Hard
Time Complexity: O(n log n + kn)
Space Complexity: O(n)

Approach:
1. Maintain two heaps to calculate the minimum cost of making
   every element in a sliding window of size x equal.
2. The max-heap (lo) stores the smaller half of the elements,
   while the min-heap (hi) stores the larger half.
3. Keep the lower heap with either the same number of elements
   as the upper heap or one extra element.
4. Use lazy deletion to remove outgoing elements efficiently.
5. The median of each window is the top of the lower heap.
   Calculate its equalization cost using the two heaps' sums.
6. Store the minimum equalization cost for every window in cost.
7. Use dynamic programming where prev[i] represents the minimum
   cost of selecting j-1 non-overlapping subarrays within the
   first i elements.
8. For each j, either skip the current element or select the
   window ending at position i.
9. Return the minimum cost after selecting exactly k
   non-overlapping subarrays.
"""

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        INF = float('inf')

        lo, hi = [], []   
        delayed = defaultdict(int)
        lo_cnt = hi_cnt = 0
        lo_sum = hi_sum = 0

        def prune(heap, neg):
            while heap:
                v = -heap[0] if neg else heap[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal lo_cnt, hi_cnt, lo_sum, hi_sum
            if lo_cnt > hi_cnt + 1:
                v = -heapq.heappop(lo)
                lo_cnt -= 1; lo_sum -= v
                heapq.heappush(hi, v)
                hi_cnt += 1; hi_sum += v
                prune(lo, True)
            elif lo_cnt < hi_cnt:
                v = heapq.heappop(hi)
                hi_cnt -= 1; hi_sum -= v
                heapq.heappush(lo, -v)
                lo_cnt += 1; lo_sum += v
                prune(hi, False)

        def add(v):
            nonlocal lo_cnt, hi_cnt, lo_sum, hi_sum
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v)
                lo_cnt += 1; lo_sum += v
            else:
                heapq.heappush(hi, v)
                hi_cnt += 1; hi_sum += v
            rebalance()

        def remove(v):
            nonlocal lo_cnt, hi_cnt, lo_sum, hi_sum
            delayed[v] += 1
            if v <= -lo[0]:
                lo_cnt -= 1; lo_sum -= v
                if v == -lo[0]:
                    prune(lo, True)
            else:
                hi_cnt -= 1; hi_sum -= v
                if hi and v == hi[0]:
                    prune(hi, False)
            rebalance()

        m = n - x + 1
        cost = [0] * m
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                med = -lo[0]
                cost[i - x + 1] = (med * lo_cnt - lo_sum) + (hi_sum - med * hi_cnt)

        prev = [0] * (n + 1) 
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]
        