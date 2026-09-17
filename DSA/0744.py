"""
Problem: Find Smallest Letter Greater Than Target
LeetCode ID: 744
Pattern: Binary Search
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
1. The letters array is sorted in non-decreasing order, so binary search
   can be used to find the smallest letter strictly greater than target.
2. Use a half-open search range [lo, hi), where hi starts at len(letters).
3. For each middle position:
   - If letters[mid] <= target, the current letter is not a valid answer,
     so search the right half by setting lo = mid + 1.
   - Otherwise, letters[mid] is greater than target and could be the answer,
     so keep it in the search range by setting hi = mid.
4. When the search ends, lo points to the first letter greater than target.
5. If no such letter exists, lo equals len(letters). Use modulo with the
   array length to wrap around and return the first letter.
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]
    