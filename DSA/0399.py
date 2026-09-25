"""
Problem: Evaluate Division
LeetCode ID: 399
Pattern: Graph / DFS / Weighted Graph
Difficulty: Medium
Time Complexity: O(Q * (V + E))
Space Complexity: O(V + E)

Approach:
1. Model the equations as a weighted directed graph.
2. For an equation a / b = v:
   - Add an edge from a to b with weight v.
   - Add an edge from b to a with weight 1 / v.
3. To answer a query src / dst, perform DFS starting from src.
4. During the traversal, maintain the product of edge weights along
   the current path.
5. If the destination is reached, the accumulated product represents
   the value of src / dst.
6. Use a visited set for each query to avoid cycles and repeated
   traversal of the same nodes.
7. If either variable does not exist in the graph, or no path connects
   the two variables, return -1.0.
8. If src and dst are the same existing variable, return 1.0.
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def solve(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited = {src}
            stack = [(src, 1.0)]
            while stack:
                node, prod = stack.pop()
                if node == dst:
                    return prod
                for nxt, w in graph[node].items():
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append((nxt, prod * w))
            return -1.0

        return [solve(a, b) for a, b in queries]