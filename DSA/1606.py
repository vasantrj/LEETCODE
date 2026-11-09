"""
Problem: Find Servers That Handled Most Number of Requests
LeetCode ID: 1606
Pattern: Heap / Priority Queue / Greedy
Difficulty: Hard
Time Complexity: O((n + k) log n)
Space Complexity: O(n + k)

Approach:
1. Initialize a min-heap free with server indices from 0 to k-1.
2. Maintain a busy min-heap containing (finish_time, virtual_id)
   for servers currently processing requests.
3. Process requests in arrival order.
4. Before handling each request, release all servers whose
   finish time is less than or equal to the current arrival time.
5. Convert each released server into a virtual ID that is the
   smallest ID greater than or equal to the current request
   index and has the same remainder when divided by k.
6. If no server is available, skip the request.
7. Otherwise, select the smallest virtual ID from the free heap.
   Its remainder modulo k identifies the actual server.
8. Increment that server's request count and push its finish
   time and virtual ID into the busy heap.
9. Find the maximum request count and return all server indices
   whose counts equal that maximum.
"""

import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))   
        heapq.heapify(free)
        busy = []          
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, vid = heapq.heappop(busy)
                real = vid % k
                new_vid = i + ((real - i) % k)
                heapq.heappush(free, new_vid)

            if not free:
                continue

            vid = heapq.heappop(free)
            real = vid % k
            count[real] += 1
            heapq.heappush(busy, (start + dur, vid))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]