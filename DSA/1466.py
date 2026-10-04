"""
Problem: Reorder Routes to Make All Paths Lead to the City Zero
LeetCode ID: 1466
Pattern: Graph / Breadth-First Search / Tree Traversal
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Treat the roads as an undirected graph for traversal, while keeping
   track of their original direction.
2. For each directed connection `a -> b`:
   - Add `(b, 1)` to `a`'s adjacency list because traveling from `a`
     to `b` follows the original direction and would need to be reversed.
   - Add `(a, 0)` to `b`'s adjacency list because traveling from `b`
     toward `a` already follows the direction needed to reach city 0.
3. Start a BFS from city 0 and mark it as visited.
4. For every unvisited neighboring city:
   - If the edge has cost `1`, its original direction points away from
     city 0, so it must be reordered.
   - Add the edge's cost to the answer.
5. Continue BFS until every city has been visited.
6. Because the original graph is a tree, every city is reached exactly
   once, and every incorrectly directed edge is counted exactly once.
"""

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  
            graph[b].append((a, 0))  

        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        changes = 0

        while queue:
            u = queue.popleft()
            for v, cost in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    changes += cost
                    queue.append(v)
        return changes