"""
Problem: Count Numbers with Unique Digits
LeetCode ID: 357
Pattern: Math / Combinatorics
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. If n == 0, only the number 0 is considered, so return 1.
2. Limit n to 10 because there are only 10 decimal digits, and no
   number with more than 10 digits can have all unique digits.
3. Start with ans = 10, which counts all numbers from 0 to 9.
4. For a k-digit number:
   - The first digit has 9 choices because it cannot be 0.
   - Each following digit has one fewer available choice because
     previously used digits cannot be repeated.
5. Start with 9 choices for the first digit and multiply by the number
   of available digits for each additional position.
6. Add the count of each valid digit length to ans.
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        n = min(n, 10)
        answer = 10
        unique_digits = 9
        available = 9
        for _ in range(2, n + 1):
            unique_digits *= available
            answer += unique_digits
            available -= 1
        return answer