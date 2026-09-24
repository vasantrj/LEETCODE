"""
Problem: Keys and Rooms
LeetCode ID: 841
Pattern: Graph Traversal / DFS / Stack
Difficulty: Medium
Time Complexity: O(n + e)
Space Complexity: O(n)

Approach:
1. Treat each room as a node in a graph and each key as an edge
   leading to another room.
2. Start from room 0 because it is initially unlocked.
3. Use a stack to perform an iterative Depth-First Search (DFS).
4. Maintain a visited set to keep track of rooms that have already
   been discovered.
5. For every room removed from the stack:
   - Examine all keys inside it.
   - If a key leads to an unvisited room, mark that room as visited
     and add it to the stack.
6. Continue until there are no more reachable rooms.
7. If the number of visited rooms equals the total number of rooms,
   every room can be visited; otherwise, some rooms remain locked.
"""

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}
        stack = [0]

        while stack:
            room = stack.pop()

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)