"""
Problem: Partition Array Into Three Parts With Equal Sum
LeetCode ID: 1013
Pattern: Arrays / Prefix Sum / Greedy
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Calculate the total sum of all elements in the array.
2. If the total sum is not divisible by 3, it is impossible to split
   the array into three parts with equal sums, so return False.
3. Calculate the required sum for each part:
   target = total // 3
4. Traverse the array while maintaining a running sum.
5. Whenever the running sum equals target:
   - One valid part has been found.
   - Increment the count of valid parts.
   - Reset the running sum to start searching for the next part.
6. If at least three parts are found, return True; otherwise, return
   False.
"""

from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        count = 0
        running_sum = 0
        for num in arr:
            running_sum += num

            if running_sum == target:
                count += 1
                running_sum = 0
        return count >= 3