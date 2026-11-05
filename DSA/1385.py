
"""
Problem: Find the Distance Value Between Two Arrays
LeetCode ID: 1385
Pattern: Sorting / Binary Search
Difficulty: Easy
Time Complexity: O(n log n + m log m)
Space Complexity: O(1) auxiliary space (excluding sorting)

Approach:
1. Sort arr2 to enable efficient binary search.
2. Iterate through each element x in arr1.
3. Use bisect_left to find the first position in arr2
   where an element is greater than or equal to x.
4. Check the element at that position, if it exists.
   If its difference from x is less than or equal to d,
   x does not satisfy the condition.
5. Check the previous element, if it exists.
   If its difference from x is less than or equal to d,
   x also does not satisfy the condition.
6. If neither neighboring element violates the condition,
   increment the distance value counter.
7. Return the final count.
"""


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)
        count = 0

        for x in arr1:
            i = bisect_left(arr2, x)
            ok = True
            if i < n and arr2[i] - x <= d:
                ok = False
            if i > 0 and x - arr2[i - 1] <= d:
                ok = False
            if ok:
                count += 1
        return count