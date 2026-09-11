"""
Problem: Unique 3-Digit Even Numbers
LeetCode ID: 3483
Pattern: Arrays / Permutations / Sets
Difficulty: Easy
Time Complexity: O(n^3)
Space Complexity: O(n^3)

Approach:
1. Generate all possible arrangements of three different indices from
   the digits array using permutations.
2. For each arrangement:
   - Skip it if the first digit is 0 because a 3-digit number cannot
     start with zero.
   - Skip it if the last digit is odd because the number must be even.
3. Construct the 3-digit number using the selected digits.
4. Store each valid number in a set so duplicate numbers created from
   repeated digits are counted only once.
5. Return the size of the set as the number of unique 3-digit even
   numbers that can be formed.
"""

from itertools import permutations
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        unique_numbers = set()
        for i, j, k in permutations(range(n), 3):
            if digits[i] == 0:
                continue

            if digits[k] % 2 != 0:
                continue

            number = (digits[i] * 100 + digits[j] * 10 + digits[k])
            unique_numbers.add(number)
        return len(unique_numbers)