
"""
Problem: Integer to Roman
LeetCode ID: 12
Pattern: Greedy / String Manipulation
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1) auxiliary space

Approach:
1. Create two lists containing Roman numeral values and
   their corresponding symbols in descending order.
2. Include special subtractive combinations such as 900 (CM),
   400 (CD), 90 (XC), 40 (XL), 9 (IX), and 4 (IV).
3. Initialize an empty list to store the Roman numeral parts.
4. Iterate through the values and symbols together.
5. Use divmod(num, v) to determine how many times the current
   Roman numeral value can be used and calculate the remainder.
6. Append the corresponding symbol repeated by that count.
7. Stop when the remaining number becomes zero.
8. Join all collected symbols and return the Roman numeral.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = []
        for v, s in zip(vals, syms):
            if num == 0:
                break
            count, num = divmod(num, v)
            res.append(s * count)
        return "".join(res)