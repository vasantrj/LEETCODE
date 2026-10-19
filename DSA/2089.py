"""
Problem: Find Target Indices After Sorting Array
LeetCode ID: 2089
Pattern: Arrays / Counting
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n) including the output

Approach:
1. Count how many elements are strictly smaller than target.
2. Count how many elements are equal to target.
3. After sorting, all elements smaller than target appear first.
   Therefore, the first target occurrence is at index less.
4. The target occupies equal consecutive positions starting at
   less and ending before less + equal.
5. Return the list of indices in that range.
"""

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = 0
        equal = 0

        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                equal += 1

        return list(range(less, less + equal))