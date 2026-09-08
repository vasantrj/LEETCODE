"""
Problem: Count Commas in Range
LeetCode ID: 3870
Pattern: Math / Counting
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. A comma appears in a number whenever the number contains at least
   four digits, such as 1,000 or 10,000.
2. For every comma position corresponding to 1,000, 1,000,000,
   1,000,000,000, and so on, count how many numbers from that point
   through n contain a comma at that position.
3. For a threshold x, all numbers from x to n contribute one comma,
   giving n - x + 1 occurrences.
4. Start with x = 1000 and repeatedly multiply x by 1000 to consider
   the next comma position.
5. Add the contribution of every comma position and return the total.
"""

class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        threshold = 1000
        while threshold <= n:
            answer += n - threshold + 1
            threshold *= 1000
        return answer