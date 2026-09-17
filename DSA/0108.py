"""
Problem: Convert Sorted Array to Binary Search Tree
LeetCode ID: 108
Pattern: Binary Tree / Divide and Conquer
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(log n)

Approach:
1. The input array is sorted in ascending order.
2. To create a height-balanced BST, choose the middle element of the
   current range as the root.
3. Recursively construct the left subtree using elements before the
   middle index.
4. Recursively construct the right subtree using elements after the
   middle index.
5. Continue dividing each range until left > right, which means there
   are no elements left to construct a node.
6. Use (left + right + 1) // 2 to select the upper middle element when
   the current range contains an even number of elements.
7. Return the root of the constructed balanced BST.
"""


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(nums) - 1)