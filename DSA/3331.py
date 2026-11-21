
"""
Problem: Find Subtree Sizes After Changes
LeetCode ID: 3331
Pattern: Tree / DFS / Postorder Traversal
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Build the children adjacency list using the original parent array.
2. Create new_parent to store the updated parent of every node.
3. Perform an iterative DFS using entering and leaving states.
4. Maintain a last array that records the most recently visited ancestor
   for each lowercase character.
5. When entering a node:
   - Save the previous last occurrence of its character.
   - If one exists, update the node's parent to that ancestor.
   - Set the current node as the latest occurrence.
6. When leaving a node, restore the previous character occurrence.
   This ensures that sibling branches do not affect each other.
7. Process nodes in postorder, accumulating each node's subtree size
   into its updated parent.
8. Return the resulting subtree sizes.
"""

from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26
        saved = [-1] * n
        post = []

        stack = [(0, False)]
        while stack:
            node, leaving = stack.pop()
            c = ord(s[node]) - 97
            if leaving:
                last[c] = saved[node]      # restore
                post.append(node)
                continue
            saved[node] = last[c]
            if last[c] != -1:
                new_parent[node] = last[c]  # closest ancestor with same char
            last[c] = node
            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))

        size = [1] * n
        for x in post:
            if x != 0:
                size[new_parent[x]] += size[x]
        return size