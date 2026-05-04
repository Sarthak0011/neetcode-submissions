# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        while head:
            ahead = head.next;
            head.next = prev
            prev = head
            head = ahead
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = slow.next
        slow.next = None

        second = self.reverse(second)

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        



