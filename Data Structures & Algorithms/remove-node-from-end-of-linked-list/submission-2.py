# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_node = ListNode(-1, head)
        slow_ptr = temp_node
        fast_ptr = temp_node

        for i in range(n):
            fast_ptr = fast_ptr.next
        
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        if slow_ptr == temp_node:
            return head.next
        
        slow_ptr.next = slow_ptr.next.next
        return head