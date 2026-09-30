"""
Problem: Lowest Common Ancestor of a Binary Tree
LeetCode ID: 236
Pattern: Binary Tree / Depth-First Search / Recursion
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. Recursively search the binary tree for nodes `p` and `q`.
2. If the current node is `None`, return `None` because neither target
   exists in that subtree.
3. If the current node is either `p` or `q`, return the current node.
   This also handles the case where one target is an ancestor of the other.
4. Recursively search both the left and right subtrees.
5. If both recursive calls return a node, then `p` and `q` were found in
   different subtrees. Therefore, the current node is their lowest common
   ancestor.
6. If only one side returns a node, propagate that node upward because
   both targets must be located within that subtree.
7. The final returned node is the lowest common ancestor of `p` and `q`.
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right