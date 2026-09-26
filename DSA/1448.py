"""
Problem: Count Good Nodes in Binary Tree
LeetCode ID: 1448
Pattern: Binary Tree / Depth-First Search
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. A node is considered good if its value is greater than or equal to
   every value encountered on the path from the root to that node.
2. Perform a DFS traversal while maintaining the maximum value seen on
   the current root-to-node path.
3. For each node:
   - Check whether `node.val >= max_so_far`.
   - If true, count the node as good.
   - Update the maximum value for the current path.
4. Recursively process the left and right subtrees using the updated
   maximum value.
5. Start the traversal with `root.val` as the initial maximum because
   the root is always a good node.
6. Add the counts from both subtrees to obtain the total number of
   good nodes.
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            count = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)