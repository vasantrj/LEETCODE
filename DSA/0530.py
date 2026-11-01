
"""
Problem: Minimum Absolute Difference in BST
LeetCode ID: 530
Pattern: Binary Search Tree / Inorder Traversal
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h), where h is the height of the tree

Approach:
1. Initialize prev to None to track the previously visited node's value.
2. Initialize ans to infinity to store the minimum difference.
3. Perform an inorder traversal of the BST.
4. Inorder traversal visits BST values in ascending order.
5. For each node, calculate the difference between its value
   and the previously visited value.
6. Update the minimum difference and move to the next node.
7. Return the minimum difference after traversal.
"""

from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)

            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.ans