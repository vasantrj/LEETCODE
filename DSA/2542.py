"""
Problem: Maximum Subsequence Score
LeetCode ID: 2542
Pattern: Greedy / Heap / Sorting
Difficulty: Medium
Time Complexity: O(n log n + n log k)
Space Complexity: O(n + k)

Approach:
1. Pair each element of nums1 with the corresponding element of nums2.
2. Sort these pairs in descending order of their nums2 values.
3. Iterate through the sorted pairs. At each position, the current
   nums2 value becomes the minimum nums2 value among the elements
   considered so far.
4. Maintain a min-heap containing the selected nums1 values and keep
   the sum of those values in `total`.
5. If the heap contains more than k elements, remove the smallest
   nums1 value. This keeps the largest k nums1 values for the current
   nums2 threshold.
6. Once exactly k elements are selected, calculate the score:
   sum(nums1) * minimum(nums2).
7. Update the maximum score found.
8. Processing nums2 values in descending order ensures that the
   current value is always the minimum nums2 value of the selected
   subsequence.
"""

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda p: -p[1])
        heap = []
        total = 0
        best = 0
        for a, b in pairs:
            heapq.heappush(heap, a)
            total += a
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, total * b)
        return best
    