"""
Problem: Leaf-Similar Trees
LeetCode ID: 872
Pattern: Binary Tree / DFS
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(n + m)

Approach:
1. Perform a depth-first traversal of each binary tree.
2. During the traversal:
   - If the current node is None, return an empty list.
   - If the node is a leaf (it has no left or right child), return its
     value as a single-element list.
   - Otherwise, recursively collect the leaves from the left and right
     subtrees.
3. The resulting list represents the tree's leaf value sequence from
   left to right.
4. Compare the leaf sequences of both trees.
5. If both sequences are identical, the trees are leaf-similar; otherwise,
   they are not.
"""


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def get_leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)
        return get_leaves(root1) == get_leaves(root2)
    