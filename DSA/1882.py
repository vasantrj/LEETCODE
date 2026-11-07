"""
Problem: Process Tasks Using Servers
LeetCode ID: 1882
Pattern: Heap / Priority Queue / Greedy
Difficulty: Medium
Time Complexity: O((n + m) log n)
Space Complexity: O(n)

Approach:
1. Create a min-heap named free containing (weight, index)
   for every available server.
2. Maintain another min-heap named busy containing
   (finish_time, weight, index) for servers processing tasks.
3. Iterate through tasks in their original order.
4. Update the current time to at least the task's arrival time.
5. If no server is free, advance the current time to the
   earliest finishing time among busy servers.
6. Move every server whose finish time is less than or equal
   to the current time from the busy heap to the free heap.
7. Select the free server with the smallest weight.
   If weights are equal, the smaller index is selected.
8. Assign the task to that server and calculate its finish time.
9. Add the assignment to the result and push the server
   into the busy heap.
10. Return the server indices assigned to all tasks.
"""


import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        res = []
        t = 0

        for j, dur in enumerate(tasks):
            t = max(t, j)
            if not free:
                t = max(t, busy[0][0])

            while busy and busy[0][0] <= t:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            res.append(i)
            heapq.heappush(busy, (t + dur, w, i))
        return res