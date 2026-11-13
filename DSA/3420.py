"""
Problem: Count Non-Decreasing Subarrays After K Operations
LeetCode ID: 3420
Pattern: Sliding Window / Monotonic Deque / Prefix Sum
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Calculate prefix sums using accumulate so that range sums
   can be obtained in O(1).
2. Maintain a monotonic deque of indices in decreasing order
   of their corresponding values.
3. Traverse the array from right to left, treating l as the
   current left boundary of the sliding window.
4. Remove deque indices from the front while their values are
   less than or equal to nums[l].
5. Before removing each index, subtract its contribution to
   the number of operations required to make the affected
   segment non-decreasing.
6. Calculate and add the contribution of the newly included
   element nums[l].
7. If the total cost exceeds k, shrink the window from the
   right until the cost becomes valid.
8. Add r - l + 1 to the answer because every subarray starting
   at l and ending between l and r satisfies the condition.
9. Return the total number of valid subarrays.
"""


from collections import deque
from itertools import accumulate
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] + list(accumulate(nums))
        dq = deque()
        cost = 0
        r = n - 1
        ans = 0
        for l in range(n - 1, -1, -1):
            while dq and nums[dq[0]] <= nums[l]:
                j = dq.popleft()
                e = dq[0] - 1 if dq else r
                cost -= (nums[j] * (e - j + 1) - (pre[e + 1] - pre[j]))
            e = dq[0] - 1 if dq else r
            cost += (nums[l] * (e - l + 1) - (pre[e + 1] - pre[l]))
            dq.appendleft(l)
            while cost > k:
                j = dq[-1]
                cost -= nums[j] - nums[r]
                if j == r:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans