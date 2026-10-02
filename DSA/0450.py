"""
Problem: Delete Node in a BST
LeetCode ID: 450
Pattern: Binary Search Tree / Recursion
Difficulty: Medium
Time Complexity: O(h)
Space Complexity: O(h)

Approach:
1. Use the BST property to locate the node containing `key`:
   - If `key < root.val`, search in the left subtree.
   - If `key > root.val`, search in the right subtree.
   - Otherwise, the current node is the node to delete.
2. If the node has no left child, return its right child to replace it.
3. If the node has no right child, return its left child to replace it.
4. If the node has two children:
   - Find its inorder successor, which is the smallest node in the
     right subtree.
   - Replace the current node's value with the successor's value.
   - Recursively delete the successor from the right subtree.
5. Return the updated root so that all recursive calls correctly reconnect
   the modified subtree.
"""


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

        return root
    