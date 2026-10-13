
"""
Problem: Maximum Alternating Sum of Squares
LeetCode ID: 3727
Pattern: Greedy / Sorting
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Square every element in nums because the objective uses squares.
2. Sort the squared values in ascending order.
3. The largest half of the squared values should contribute
   positively, while the smallest half should contribute negatively.
4. Calculate the difference between the sum of the larger half
   and the sum of the smaller half.
5. When n is odd, the larger half contains one extra element,
   which contributes positively.
"""


from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        k = n // 2
        return sum(sq[k:]) - sum(sq[:k])
