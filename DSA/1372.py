"""
Problem: Longest ZigZag Path in a Binary Tree
LeetCode ID: 1372
Pattern: Binary Tree / Depth-First Search / Recursion
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. A ZigZag path alternates between moving left and right at every step.
2. Use DFS while tracking:
   - `go_left`: the direction of the next move.
   - `length`: the current ZigZag path length.
3. At each node, update the global maximum with the current path length.
4. If the next move should be left:
   - Continue the current ZigZag through the left child.
   - Start a new ZigZag from the right child with length 1.
5. If the next move should be right:
   - Continue the current ZigZag through the right child.
   - Start a new ZigZag from the left child with length 1.
6. Start DFS from both children of the root because either direction can
   be the first move.
7. The longest path found during the traversal is the answer.
"""


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def dfs(node, go_left, length):
            if not node:
                return
            self.best = max(self.best, length)
            if go_left:
                dfs(node.left, False, length + 1)   
                dfs(node.right, True, 1)         
            else:
                dfs(node.right, True, length + 1)   
                dfs(node.left, False, 1)        

        dfs(root.left, False, 1)
        dfs(root.right, True, 1)
        return self.best

    