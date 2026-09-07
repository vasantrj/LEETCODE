"""
Problem: Bitwise ORs of Subarrays
LeetCode ID: 898
Pattern: Bit Manipulation / Arrays / Hashing
Difficulty: Medium
Time Complexity: O(n * B)
Space Complexity: O(n * B)

Approach:
1. Maintain cur, the set of all distinct bitwise OR values of
   subarrays ending at the current position.
2. For each number num:
   - Start a new subarray containing only num.
   - Extend every subarray that ended at the previous position by
     applying bitwise OR with num.
   - Store the resulting distinct OR values in cur.
3. Add all values in cur to result, which stores every distinct
   bitwise OR value found across all subarrays.
4. The number of distinct OR values is the size of result.
5. The number of distinct values in cur is bounded by the number of
   bits because repeatedly applying OR can only change a bit from 0
   to 1 and never back to 0.

"""

from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()
        for num in arr:
            current = {num | value for value in current} | {num}
            result |= current
        return len(result)