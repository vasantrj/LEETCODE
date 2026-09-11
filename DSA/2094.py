"""
Problem: Finding 3-Digit Even Numbers
LeetCode ID: 2094
Pattern: Arrays / Counting / Frequency
Difficulty: Easy
Time Complexity: O(n + 450)
Space Complexity: O(1)

Approach:
1. Build a frequency array where count[d] stores how many times digit
   d appears in the input.
2. Generate every possible 3-digit even number from 100 to 998.
3. For each candidate number:
   - Extract its hundreds, tens, and units digits.
   - Build a frequency array for the three required digits.
4. Check whether the required frequency of every digit is less than
   or equal to its available frequency in the input.
5. If enough digits are available, add the candidate number to result.
6. Since the candidates are checked in increasing order, result is
   automatically returned in ascending order.
"""

from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = [0] * 10
        for digit in digits:
            count[digit] += 1

        result = []
        for number in range(100, 1000, 2):
            hundreds = number // 100
            tens = (number // 10) % 10
            units = number % 10
            required = [0] * 10
            required[hundreds] += 1
            required[tens] += 1
            required[units] += 1
            if all(required[i] <= count[i] for i in range(10)):
                result.append(number)
        return result