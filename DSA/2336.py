"""
Problem: Smallest Number in Infinite Set
LeetCode ID: 2336
Pattern: Heap / Hash Set / Design
Difficulty: Medium
Time Complexity: O(log n) for addBack and O(log n) for popSmallest
Space Complexity: O(n)

Approach:
1. The infinite set initially contains all positive integers starting
   from 1.
2. Maintain `cur` as the smallest number that has never been removed
   from the original infinite sequence.
3. Maintain a min-heap for numbers that were removed and later added
   back using `addBack`.
4. Maintain a `seen` set to prevent the same number from being added
   to the heap more than once.
5. For `popSmallest`:
   - If the heap is non-empty, its minimum value is the smallest
     available number, so remove and return it.
   - Otherwise, return `cur` and increment it.
6. For `addBack`:
   - A number only needs to be added back if it is smaller than `cur`,
     meaning it has previously been removed.
   - Check `seen` to avoid duplicate entries in the heap.
7. This separates the untouched infinite sequence from numbers that have
   been explicitly removed and restored.
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self) -> int:
        if self.heap:
            value = heapq.heappop(self.heap)
            self.seen.remove(value)
            return value

        value = self.cur
        self.cur += 1

        return value

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)