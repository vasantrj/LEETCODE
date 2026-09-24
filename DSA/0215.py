"""
Problem: Kth Largest Element in an Array
LeetCode ID: 215
Pattern: Heap / Priority Queue
Difficulty: Medium
Time Complexity: O(n log k)
Space Complexity: O(k)

Approach:
1. Maintain a min-heap containing the k largest elements seen so far.
2. Initialize the heap with the first k elements of the array and
   convert it into a min-heap using heapify().
3. The smallest element in this heap represents the current kth
   largest element.
4. Traverse the remaining elements:
   - If the current element is larger than the smallest element in
     the heap, replace the smallest element with the current element.
   - Otherwise, ignore the current element because it cannot belong
     to the k largest elements.
5. After processing the entire array, the heap contains the k largest
   elements.
6. The smallest element in the heap is therefore the kth largest
   element.
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]