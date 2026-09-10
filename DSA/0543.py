"""
Problem: Diameter of Binary Tree
LeetCode ID: 543
Pattern: Binary Tree / DFS / Postorder Traversal
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. Perform a postorder DFS traversal to calculate the height of each
   subtree.
2. For each node:
   - Calculate the height of its left subtree.
   - Calculate the height of its right subtree.
3. The longest path passing through the current node has a length of:
   left_height + right_height
   because the height represents the number of edges from the node
   to its deepest descendant.
4. Update the maximum diameter seen so far using this value.
5. Return the height of the current subtree:
   1 + max(left_height, right_height)
6. After processing the entire tree, return the maximum diameter found.
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            # returns height of subtree rooted at node
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # diameter through this node = left_height + right_height (edges)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter