"""
Problem: Count Nodes Equal to Average of Subtree
LeetCode ID: 2265
Pattern: Binary Tree / DFS / Postorder Traversal
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. Traverse the binary tree using postorder DFS so that the sum and
   count of nodes in both subtrees are calculated before processing
   the current node.
2. For each node:
   - Recursively calculate the sum and count of the left subtree.
   - Recursively calculate the sum and count of the right subtree.
   - Add the current node's value to obtain the total subtree sum.
   - Add 1 to obtain the total number of nodes in the subtree.
3. Calculate the integer average of the subtree using:
   total_sum // total_count
4. If the average equals the current node's value, increment the count.
5. Return the total sum and node count to the parent node so they can
   be used to calculate the parent's subtree information.
6. Return the final count after processing the entire tree.
"""

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_sum // total_count == node.val:
                self.count += 1
            return total_sum, total_count
        dfs(root)
        return self.count