
"""
Problem: Maximize Sum of Squares of Digits
LeetCode ID: 3723
Pattern: Greedy
Difficulty: Medium
Time Complexity: O(num)
Space Complexity: O(num)

Approach:
1. Check whether the required digit sum exceeds 9 * num.
   If it does, return an empty string because no valid number exists.
2. Divide the required sum by 9 to determine how many digits
   can be set to 9, maximizing the sum of squared digits.
3. Use the remainder as the next nonzero digit, if one exists.
4. Append zeros until the result contains exactly num digits.
5. Return the resulting string.
"""


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        k, r = divmod(sum, 9)
        res = "9" * k
        if r:
            res += str(r)
        return res + "0" * (num - len(res))
    