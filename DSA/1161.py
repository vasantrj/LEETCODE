"""
Problem: Maximum Level Sum of a Binary Tree
LeetCode ID: 1161
Pattern: Binary Tree / Breadth-First Search / Level Order Traversal
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use Breadth-First Search (BFS) to traverse the binary tree level by
   level.
2. Maintain `level` to track the current level number, starting from 1.
3. For each level:
   - Process all nodes currently in the queue.
   - Add their values to `level_sum`.
   - Add their non-null children to the queue for the next level.
4. Maintain `best_sum` as the largest level sum encountered so far and
   `best_level` as the corresponding level number.
5. Update the best answer only when the current level sum is strictly
   greater than the previous best sum.
6. Because levels are processed from top to bottom, keeping the first
   occurrence of the maximum automatically satisfies the requirement to
   return the smallest level number in case of a tie.
"""


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        best_sum = float("-inf")
        best_level = 0
        level = 0

        while queue:
            level += 1
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level

        return best_level