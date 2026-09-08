"""
Problem: Nth Digit
LeetCode ID: 400
Pattern: Math / Digit Counting / Number Ranges
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. Group positive integers by their number of digits:
   - 1-digit numbers: 1 to 9
   - 2-digit numbers: 10 to 99
   - 3-digit numbers: 100 to 999
   - and so on.
2. For each digit-length group, calculate how many digits it
   contributes using digits * count.
3. Subtract complete groups from n until n falls inside the target
   digit-length group.
4. Calculate the exact number containing the nth digit:
   - (n - 1) // digits gives the offset of the target number.
   - Add this offset to start.
5. Calculate the position of the required digit inside that number
   using (n - 1) % digits.
6. Convert the target number to a string and return the digit at the
   calculated position.
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        number = start + (n - 1) // digits
        digit_index = (n - 1) % digits
        return int(str(number)[digit_index])