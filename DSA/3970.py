"""
Problem: Shortest Path With At Most K Consecutive Identical Characters
LeetCode ID: 3970
Pattern: Graph / Dijkstra on an Expanded State Space (node, current run length)
Difficulty: Medium (not verified; adjust if LeetCode lists it differently)
Time Complexity: O(k * (n + m) * log(n * k))
Space Complexity: O(n * k + m)

Approach:
1. Build a directed adjacency list from edges (u -> v with weight w).
2. The cost of a path depends only on edge weights, but whether a move is
   legal depends on how many consecutive nodes with the same label we have
   just visited. So a plain node-only Dijkstra is not enough, and the state
   must be (node, run), where run is the length of the current streak of
   identical labels ending at that node.
3. Flatten the state into one index: idx = node * (k + 1) + run, with
   run in [1, k]. Slot 0 of each block is unused so that run can index
   directly without an offset.
4. Start at node 0 with run = 1 (the starting node itself counts as the first
   character) and distance 0.
5. Transition along an edge u -> v with weight w:
   - labels[v] == labels[u]: the streak grows, nr = run + 1. If nr > k, the
     move is illegal, so skip it.
   - labels[v] != labels[u]: the streak resets, nr = 1.
   The new distance is d + w.
6. Run standard Dijkstra with a min-heap over (dist, node, run). Skip stale
   heap entries when d > dist[state]. Since all weights are non-negative, the
   first time node n - 1 is popped, in any run state, d is the shortest
   valid distance, so return it immediately.
7. If the heap empties without reaching n - 1, no valid path exists: return -1.
"""


import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')
        K = k + 1
        dist = [INF] * (n * K)  
        dist[0 * K + 1] = 0
        pq = [(0, 0, 1)]        

        while pq:
            d, u, run = heapq.heappop(pq)
            if d > dist[u * K + run]:
                continue
            if u == n - 1:
                return d       
            lu = labels[u]
            for v, w in adj[u]:
                if labels[v] == lu:
                    nr = run + 1
                    if nr > k:
                        continue
                else:
                    nr = 1
                nd = d + w
                idx = v * K + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(pq, (nd, v, nr))
        return -1