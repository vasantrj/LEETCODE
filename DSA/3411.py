"""
Problem: Maximum Subarray With Equal Products
LeetCode ID: 3411
Pattern: Brute Force / Running Aggregates
Difficulty: Easy
Time Complexity: O(n^2 log M)
Space Complexity: O(1)

Approach:
1. A subarray is valid when product == gcd * lcm.
2. Fix the left index i and extend the right index j, keeping a
   running product, gcd and lcm so each extension is incremental.
3. Update gcd with gcd(g, x) and lcm with l * x // gcd(l, x).
4. Whenever product == gcd * lcm, update the best length.
5. Return the best length found (n <= 100, so O(n^2) is fine).
"""


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        for i in range(n):
            prod, g, l = 1, 0, 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if prod == g * l:
                    best = max(best, j - i + 1)

        return best
    