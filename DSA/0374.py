"""
Problem: Guess Number Higher or Lower
LeetCode ID: 374
Pattern: Binary Search
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. The hidden number is guaranteed to be within the range [1, n].
2. Use binary search to repeatedly check the middle number.
3. Call guess(mid) to determine the relationship between mid and the
   hidden number:
   - If the result is 0, mid is the hidden number, so return it.
   - If the result is negative, mid is greater than the hidden number,
     so search the left half by setting right = mid - 1.
   - If the result is positive, mid is smaller than the hidden number,
     so search the right half by setting left = mid + 1.
4. Continue until the hidden number is found or the search range becomes
   empty.
5. Return -1 if no valid number is found.
"""


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    