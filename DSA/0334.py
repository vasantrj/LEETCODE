"""
Problem: Increasing Triplet Subsequence
LeetCode ID: 334
Pattern: Greedy / Array
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. We need to determine whether there exist three indices i < j < k
   such that nums[i] < nums[j] < nums[k].
2. Maintain two variables:
   - first: the smallest value seen so far.
   - second: the smallest possible value that can serve as the second
     element of an increasing triplet.
3. Traverse the array from left to right.
4. For each number n:
   - If n <= first, update first because n is a better candidate for
     the smallest first element.
   - Else if n <= second, update second because n can form a smaller
     increasing pair with first.
   - Otherwise, n is greater than both first and second, meaning an
     increasing triplet has been found.
5. If the traversal finishes without finding such a third value, return
   False.
6. Only two values are maintained, so the solution uses constant space.
"""


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False