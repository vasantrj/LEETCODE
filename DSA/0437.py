"""
Problem: Path Sum III
LeetCode ID: 437
Pattern: Binary Tree / Prefix Sum / Hashing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(h)

Approach:
1. A valid path can start and end at any nodes, but it must follow
   parent-to-child connections.
2. Maintain a `running_sum` representing the sum from the root of the
   current DFS path to the current node.
3. Store the frequency of every prefix sum encountered on the current
   root-to-node path in a hash map.
4. For the current node, if:
   `running_sum - targetSum`
   has appeared before, then the difference between those two prefix
   sums represents a path whose sum equals `targetSum`.
5. Add the frequency of that required prefix sum to the answer.
6. Add the current `running_sum` to the prefix-sum map before exploring
   the children.
7. After processing both children, remove the current prefix sum from
   the map so that it is not used by paths from a different branch.
8. Initialize the map with `{0: 1}` to handle paths that start directly
   at the root of the current traversal.
"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = {0: 1} 
        self.count = 0

        def dfs(node, running_sum):
            if not node:
                return
            running_sum += node.val
            self.count += prefix_counts.get(running_sum - targetSum, 0)

            prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            prefix_counts[running_sum] -= 1
            if prefix_counts[running_sum] == 0:
                del prefix_counts[running_sum]

        dfs(root, 0)
        return self.count

        