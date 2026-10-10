"""
Problem: Koko Eating Bananas
LeetCode ID: 875
Pattern: Binary Search / Search on Answer
Difficulty: Medium
Time Complexity: O(n log M)
Space Complexity: O(1)

Approach:
1. Koko must eat at least one banana per hour, so the minimum possible
   eating speed is 1.
2. The maximum useful speed is `max(piles)`, because eating at this speed
   finishes every pile in at most one hour.
3. Use binary search over the possible eating speeds.
4. For a candidate speed `mid`, calculate the hours required for every
   pile using ceiling division:
   `(pile + mid - 1) // mid`.
5. If the total hours are at most `h`, the speed is sufficient. Record
   it as a possible answer and search for a smaller speed.
6. Otherwise, the speed is too slow, so increase the lower bound.
7. When the search converges, `lo` is the minimum feasible eating speed.
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo