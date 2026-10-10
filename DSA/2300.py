"""
Problem: Successful Pairs of Spells and Potions
LeetCode ID: 2300
Pattern: Binary Search / Sorting
Difficulty: Medium
Time Complexity: O(m log m + n log m)
Space Complexity: O(log m) auxiliary space for sorting, excluding output

Approach:
1. Sort the `potions` array in ascending order so that binary search
   can efficiently locate the first successful potion.
2. For each spell `s`, a potion with strength `p` is successful when:
   `s * p >= success`.
3. Rearrange the condition to find the minimum required potion strength:
   `p >= ceil(success / s)`.
4. Calculate the ceiling using integer arithmetic:
   `(success + s - 1) // s`.
5. Use `bisect_left` to find the first potion whose strength is at
   least the required value.
6. Every potion from that index to the end forms a successful pair.
   Therefore, the count is `m - index`.
7. Append the count for each spell and return the result in the
   original order of `spells`.
"""


from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            need = (success + s - 1) // s   # ceil(success / s)
            res.append(m - bisect_left(potions, need))
        return res

    