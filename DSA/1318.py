
"""
Problem: Minimum Flips to Make a OR b Equal to c
LeetCode ID: 1318
Pattern: Bit Manipulation
Difficulty: Medium
Time Complexity: O(log(max(a, b, c)))
Space Complexity: O(1)

Approach:
1. Initialize flips to zero to count the required bit changes.
2. Process the least significant bit of a, b, and c in each iteration.
3. If the current bit of c is 0, both corresponding bits of a and b
   must be 0. Add x + y to count the required flips.
4. If the current bit of c is 1, at least one of the corresponding
   bits of a or b must be 1. If both are 0, add one flip.
5. Right-shift all three numbers to process the next bit.
6. Stop when all three numbers become zero and return flips.
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            x, y, z = a & 1, b & 1, c & 1
            if z == 0:
                flips += x + y
            elif x == 0 and y == 0:
                flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
        