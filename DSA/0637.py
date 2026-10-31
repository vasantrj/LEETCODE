"""
Problem: Average of Levels in Binary Tree
LeetCode ID: 637
Pattern: Binary Tree / Breadth-First Search (BFS)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If the root is None, return an empty list.
2. Initialize a queue with the root node to perform level-order
   traversal.
3. For each level, determine the number of nodes currently in
   the queue and initialize the level sum to zero.
4. Process exactly level_size nodes, adding their values to
   level_sum.
5. Add each node's non-null left and right children to the queue.
6. Calculate the average by dividing level_sum by level_size.
7. Append the average to the result and continue until the
   queue becomes empty.
8. Return the list of level averages.
"""


from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result
