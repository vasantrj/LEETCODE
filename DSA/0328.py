"""
Problem: Odd Even Linked List
LeetCode ID: 328
Pattern: Linked List / Two Pointers
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. The goal is to group all nodes at odd positions first, followed by
   all nodes at even positions, while preserving their original order.
2. Handle the cases where the list is empty or contains only one node.
3. Maintain two pointers:
   - odd points to the last node in the odd-positioned list.
   - even points to the last node in the even-positioned list.
4. Store the first even node in even_head because the even list will be
   connected after the odd list at the end.
5. While there are enough nodes to continue:
   - Connect the current odd node to the next even node.
   - Move odd to the newly connected odd-positioned node.
   - Connect the current even node to the next odd node.
   - Move even to the newly connected even-positioned node.
6. After separating the two groups, connect the end of the odd list to
   even_head.
7. Return head, which is still the first node of the reordered list.
8. The list is rearranged in-place without creating additional nodes.
"""


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even  
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head 
        return head