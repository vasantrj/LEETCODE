"""
Problem: Search in a Binary Search Tree
LeetCode ID: 700
Pattern: Binary Search Tree / Recursion
Difficulty: Easy
Time Complexity: O(h)
Space Complexity: O(h)

Approach:
1. Start searching from the root of the Binary Search Tree.
2. If the current node is None, the target value does not exist in the
   tree, so return None.
3. If the current node's value equals val, return the current node because
   the required subtree has been found.
4. If val is smaller than the current node's value, use the BST property
   to search only the left subtree.
5. If val is greater than the current node's value, search only the right
   subtree.
6. Continue recursively until the target is found or the search reaches
   an empty subtree.
"""


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        