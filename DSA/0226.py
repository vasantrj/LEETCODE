
"""
Problem: Invert Binary Tree
LeetCode ID: 226
Pattern: Binary Tree / Breadth-First Search (BFS)
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. If the root is None, return None because the tree is empty.
2. Initialize a queue with the root node to perform level-order traversal.
3. Remove the front node from the queue.
4. Swap its left and right children to invert that node.
5. Add the non-null children to the queue for further processing.
6. Continue until the queue is empty and return the original root,
   which now represents the inverted tree.
"""


from collections import deque
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root