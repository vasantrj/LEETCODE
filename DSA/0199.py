"""
Problem: Binary Tree Right Side View
LeetCode ID: 199
Pattern: Binary Tree / Breadth-First Search / Level Order Traversal
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If the tree is empty, return an empty list.
2. Use Breadth-First Search (BFS) with a queue to process the tree
   level by level.
3. At the beginning of each level, record the number of nodes currently
   in the queue as `level_size`.
4. Process exactly `level_size` nodes so that only nodes belonging to
   the current level are considered.
5. The last node processed at each level is the rightmost node, so add
   its value to the result.
6. Add the left and right children of each node to the queue for the
   next level.
7. Continue until every level has been processed.
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result