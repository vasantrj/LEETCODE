
"""
Problem: Remove Duplicates from Sorted Array II
LeetCode ID: 80
Pattern: Two Pointers / In-Place Array
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. If the array contains two or fewer elements, return its length
   because every element can appear at most twice.
2. Initialize k = 2 to represent the next position where
   a valid element should be placed.
3. Iterate through the array starting from index 2.
4. Compare the current element with nums[k - 2].
5. If they are different, the current element can be included
   without allowing more than two occurrences.
6. Place the current element at nums[k] and increment k.
7. Return k as the length of the modified array.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k
