"""
Problem: Minimum Depth of Binary Tree
LeetCode ID: 111
Pattern: Binary Tree / Breadth-First Search
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If the root is `None`, the tree is empty, so return 0.
2. Use Breadth-First Search (BFS) with a queue, starting from the root
   at depth 1.
3. Process nodes level by level.
4. The first node encountered that has no left or right child is a leaf.
   Since BFS visits nodes in increasing order of depth, this is guaranteed
   to be the nearest leaf from the root.
5. Add each existing child to the queue with its depth increased by 1.
6. Return the depth as soon as the first leaf node is found.
"""


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return 0
    