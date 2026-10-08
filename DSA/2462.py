"""
Problem: Total Cost to Hire K Workers
LeetCode ID: 2462
Pattern: Heap / Two Pointers / Greedy
Difficulty: Medium
Time Complexity: O(n + k log candidates)
Space Complexity: O(candidates)

Approach:
1. Use two min-heaps to represent the available candidates from the
   left and right sides of the array.
2. Initialize the left heap with up to `candidates` workers from the
   beginning of the array.
3. Initialize the right heap with up to `candidates` workers from the
   end of the array, ensuring the two candidate ranges do not overlap.
4. For each of the `k` hiring rounds:
   - Compare the smallest worker from the left and right heaps.
   - Hire the cheaper worker. If both costs are equal, choose the left
     worker as required by the problem.
5. After hiring from one side, if there are still unprocessed workers
   between `left` and `right`, add the next worker from that same side
   to its heap.
6. Continue until exactly `k` workers have been hired.
7. The heaps ensure that the minimum available cost from each side can
   be selected efficiently.
"""

import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        left, right = 0, n - 1
        lh, rh = [], []

        while left < candidates and left <= right:
            heapq.heappush(lh, costs[left])
            left += 1
        while right >= n - candidates and right >= left:
            heapq.heappush(rh, costs[right])
            right -= 1

        total = 0
        for _ in range(k):
            if not rh or (lh and lh[0] <= rh[0]):
                total += heapq.heappop(lh)
                if left <= right:
                    heapq.heappush(lh, costs[left])
                    left += 1
            else:
                total += heapq.heappop(rh)
                if left <= right:
                    heapq.heappush(rh, costs[right])
                    right -= 1
        return total