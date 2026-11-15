
"""
Problem: Number of Sub-arrays With Odd Sum
LeetCode ID: 1524
Pattern: Prefix Sum / Parity / Counting
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize MOD to 10^9 + 7 to keep the answer within
   the required modulo.
2. Maintain two counters:
   - odd: Number of previous prefix sums with odd parity.
   - even: Number of previous prefix sums with even parity.
3. Initialize even = 1 because the empty prefix has an
   even sum.
4. Maintain parity to track whether the current prefix sum
   is odd or even.
5. For each element, update parity using XOR with x & 1.
6. If the current prefix sum is odd, every previous even
   prefix sum creates a subarray with an odd sum.
   Add even to the answer and increment odd.
7. Otherwise, every previous odd prefix sum creates a
   subarray with an odd sum.
   Add odd to the answer and increment even.
8. Return the answer modulo MOD.
"""

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd, even = 0, 1
        parity = 0
        ans = 0
        for x in arr:
            parity ^= x & 1
            if parity:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % MOD