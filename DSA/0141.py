
"""
Problem: Linked List Cycle
LeetCode ID: 141
Pattern: Linked List / Two Pointers / Floyd's Cycle Detection
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize two pointers, slow and fast, at the head of the
   linked list.
2. Move slow one node forward and fast two nodes forward
   during each iteration.
3. If the linked list contains a cycle, the fast pointer will
   eventually catch up with the slow pointer.
4. If both pointers reference the same node, return True.
5. If fast or fast.next becomes None, the linked list has
   reached its end, so return False.
"""

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False