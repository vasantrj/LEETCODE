
"""
Problem: Calculate Digit Sum of a String
LeetCode ID: 2243
Pattern: String Manipulation / Simulation
Difficulty: Easy
Time Complexity: O(n log_k(n)) approximately
Space Complexity: O(n)

Approach:
1. Continue processing while the length of the string is
   greater than k.
2. Create an empty list to store the digit sums of each group.
3. Divide the string into consecutive groups of size k.
4. Calculate the sum of the digits in each group.
5. Convert each group sum into a string and append it to parts.
6. Join all group sums to create the updated string.
7. Repeat the process until the string length is at most k.
8. Return the final string.
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                parts.append(str(sum(int(c) for c in s[i:i + k])))
            s = "".join(parts)
        return s