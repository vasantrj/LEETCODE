
"""
Problem: Combination Sum III
LeetCode ID: 216
Pattern: Backtracking
Difficulty: Medium
Time Complexity: O(C(9, k) * k)
Space Complexity: O(k) auxiliary space, excluding output

Approach:
1. Use backtracking to build combinations of distinct numbers from 1 to 9.
2. Start each recursive call from the next available number to
   ensure numbers are used only once and combinations stay ordered.
3. Track the remaining target sum after choosing each number.
4. When the combination contains k numbers, add it to the result
   only if the remaining sum is zero.
5. Stop exploring a branch when a number exceeds the remaining sum.
6. Backtrack by removing the last chosen number before trying
   the next candidate.
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, path = [], []

        def backtrack(start, remaining):
            if len(path) == k:
                if remaining == 0:
                    res.append(path[:])
                return
            for num in range(start, 10):
                if num > remaining:  # later numbers are even larger
                    break
                path.append(num)
                backtrack(num + 1, remaining - num)
                path.pop()

        backtrack(1, n)
        return res