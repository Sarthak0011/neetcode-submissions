# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _find_length(self, head: Optional[ListNode]) -> int:
        len = 0
        while head:
            len += 1
            head = head.next
        return len

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self._find_length(head)
        k = l - n
        temp = head
        prev = None
        while k:
            k -= 1
            prev = temp
            temp = temp.next

        if not prev:
            return temp.next
        prev.next = temp.next
        temp.next = None
        return head

        