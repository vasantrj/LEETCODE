
"""
Problem: Minimum Operations to Sort a Permutation
LeetCode ID: 3942
Pattern: Permutations / Cyclic Patterns / Greedy
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Check whether the permutation follows a cyclic increasing
   pattern, where each next element is (current + 1) modulo n.
2. Check whether it follows a cyclic decreasing pattern, where
   each next element is (current - 1) modulo n.
3. Let k be the first element of the permutation.
4. If the permutation is cyclically increasing, calculate the
   minimum operations using k and the problem's operation rules.
5. If it is cyclically decreasing, calculate the candidate cost
   from the shifted position s = (k + 1) modulo n.
6. Take the minimum valid candidate. If neither pattern matches,
   return -1.
"""


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        inc = all(nums[(i + 1) % n] == (nums[i] + 1) % n for i in range(n))
        dec = all(nums[(i + 1) % n] == (nums[i] - 1) % n for i in range(n))

        k = nums[0]
        ans = float('inf')

        if inc:
            if k == 0:
                ans = 0
            else:
                ans = min(n - k, k + 2)

        if dec:
            s = (k + 1) % n
            ans = min(ans, 1 + min(s, (n - s) % n))

        return -1 if ans == float('inf') else ans