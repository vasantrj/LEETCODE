"""
Problem: Number of Provinces
LeetCode ID: 547
Pattern: Graph / Depth-First Search / Connected Components
Difficulty: Medium
Time Complexity: O(n²)
Space Complexity: O(n)

Approach:
1. Treat each city as a node in an undirected graph, where
   `isConnected[i][j] == 1` means there is a direct connection between
   cities `i` and `j`.
2. Maintain a `visited` array to keep track of cities that have already
   been explored.
3. Iterate through every city:
   - If the city is unvisited, it belongs to a new province.
   - Start a DFS from that city to visit every city connected to it.
4. During DFS, mark the current city as visited and inspect all other
   cities to find its directly connected neighbors.
5. Every DFS traversal completely explores one connected component,
   which corresponds to one province.
6. Count the number of DFS traversals to obtain the total number of
   provinces.
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(i: int) -> None:
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1
        return provinces
        